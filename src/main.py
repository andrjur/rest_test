from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Модель задачи
class Task(BaseModel):
    id: int
    title: str
    status: str = "Новая задача"

# Временное хранилище для задач (для примера)
tasks_db = []

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    # Добавление задачи в базу данных (временное хранилище для примера)
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    # Поиск задачи по ID
    task = next((task for task in tasks_db if task.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@app.get("/tasks", response_model=List[Task])
async def get_tasks(status: Optional[str] = None):
    # Фильтрация задач по статусу
    if status:
        filtered_tasks = [task for task in tasks_db if task.status == status]
        return filtered_tasks
    return tasks_db