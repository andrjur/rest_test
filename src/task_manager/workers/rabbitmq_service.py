import aio_pika
import asyncio

async def send_task(task_data):
    connection = await aio_pika.connect_robust("amqp://myuser:123@localhost/")
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=task_data.encode()),
            routing_key="task_queue",
        )

async def process_task(message: aio_pika.IncomingMessage):
    async with message.process():
        task_data = message.body.decode()
        print(f"Обработка задачи: {task_data}")
        # Эмуляция выполнения задачи
        await asyncio.sleep(random.randint(5, 10))
        print(f"Задача {task_data} завершена.")