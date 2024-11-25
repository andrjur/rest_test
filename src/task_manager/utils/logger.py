import logging

logging.basicConfig(level=logging.INFO)

def log_task_status(task_id, status):
    logging.info(f"Задача {task_id} изменена на статус: {status}")