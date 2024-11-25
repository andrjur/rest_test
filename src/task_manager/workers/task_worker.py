import asyncio
import aio_pika

async def process_task(message: aio_pika.IncomingMessage):
    async with message.process():
        task_data = message.body.decode()
        print(f"Обработка задачи: {task_data}")
        await asyncio.sleep(random.randint(5, 10))
        print(f"Задача {task_data} завершена.")