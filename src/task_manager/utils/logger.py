import logging
import os

# Создание директории для логов, если она не существует
os.makedirs('logs', exist_ok=True)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),  # Логи будут записываться в файл app.log
        logging.StreamHandler()  # Логи также будут выводиться в консоль
    ]
)

logger = logging.getLogger(__name__)