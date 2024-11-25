from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    status: str = "Новая задача"

@app.post("/tasks")
async def create_task(task: Task):
    # Логика для добавления задачи в базу данных
    pass

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    # Логика для получения информации о задаче
    pass

@app.get("/tasks")
async def get_tasks(status: str = None):
    # Логика для получения списка задач с фильтрацией по статусу
    pass