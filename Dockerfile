# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения в контейнер
COPY ./src /app/src

# Указываем команду для запуска приложения
CMD ["uvicorn", "src.task_manager.main:app", "--host", "0.0.0.0", "--port", "80"]