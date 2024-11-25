from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api.routes import router  # Импортируем маршруты
from .database import engine, Base  # Импортируем базу данных
from .utils.logger import logger  # Импортируем логгер

# Создаем базу данных (если это необходимо)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="src/task_manager/static"), name="static")

@app.on_event("startup")
async def startup_event():
    logger.info("Запуск приложения...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Остановка приложения...")

# Подключаем маршруты
app.include_router(router)