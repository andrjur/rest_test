from sqlalchemy import Column, Integer, String
from database import Base  # Предполагается, что у вас есть файл с настройками базы данных

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(String, default="Новая задача")