import asyncio
import aio_pika
import random
from ..utils.logger import logger  # Импортируем логгер


async def main():
    #connection = await aio_pika.connect_robust("amqp://myuser:123@localhost/")
    #connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    connection = await aio_pika.connect_robust("amqp://john:qq23@localhost/")
    logger.info(f"Ну это")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("task_queue")

        async for message in queue:
            await process_task(message)


async def process_task(message: aio_pika.IncomingMessage):
    async with message.process():
        task_data = message.body.decode()
        logger.info(f"Обработка задачи: {task_data}")

        # Эмуляция выполнения задачи с задержкой
        delay = random.randint(5, 10)
        await asyncio.sleep(delay)

        success = random.choice([True, False])  # Эмуляция успеха или ошибки
        if success:
            logger.info(f"Задача {task_data} завершена успешно.")
        else:
            logger.error(f"Ошибка при обработке задачи {task_data}.")