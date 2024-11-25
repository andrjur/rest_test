from fastapi import APIRouter
from typing import List, Optional
from ..schemas import Task  # Используйте относительный импорт для схем

router = APIRouter()

@router.post("/tasks", response_model=Task)
async def create_task(task: Task):
    # Логика добавления задачи
    pass

@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    # Логика получения задачи по ID
    pass

@router.get("/tasks", response_model=List[Task])
async def get_tasks(status: Optional[str] = None):
    # Логика получения списка задач с фильтрацией по статусу
    pass