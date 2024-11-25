from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from ..schemas import Task, TaskCreate  # Импортируем схемы
from ..models import TaskModel  # Импортируем модель базы данных
from ..database import get_db  # Импортируем функцию для получения сессии базы данных
from ..workers.rabbitmq_service import send_task  # Импортируем функцию отправки задачи
from ..utils.logger import logger  # Импортируем логгер

router = APIRouter()


@router.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Создаем новую задачу в базе данных
    logger.info(f"Создание задачи с заголовком: {task.title}")
    task_model = TaskModel(title=task.title)
    db.add(task_model)
    db.commit()
    db.refresh(task_model)

    # Отправляем задачу в очередь RabbitMQ
    await send_task(task_model.title)  # Отправляем заголовок задачи
    logger.info(f"Задача создана с ID: {task_model.id}")
    return task_model


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    # Получаем задачу по ID из базы данных
    logger.info(f"Получение задачи с ID: {task_id}")
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    return task


@router.get("/tasks", response_model=List[Task])
async def get_tasks(status: Optional[str] = None, db: Session = Depends(get_db)):
    # Получаем список задач с фильтрацией по статусу
    logger.info(f"Получение списка задач с фильтром по статусу: {status}")
    if status:
        tasks = db.query(TaskModel).filter(TaskModel.status == status).all()
    else:
        tasks = db.query(TaskModel).all()

    logger.info(f"Найдено задач: {len(tasks)}")
    return tasks