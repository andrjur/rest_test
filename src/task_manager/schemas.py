from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    status: str = "Новая задача"

    class Config:
        orm_mode = True  # Позволяет использовать модели SQLAlchemy