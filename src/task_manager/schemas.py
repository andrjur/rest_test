from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    status: str = "Новая задача"

    class Config:
        #orm_mode = True  # Позволяет использовать модели SQLAlchemy
        from_attributes = True  # Заменили orm_mode на from_attributes