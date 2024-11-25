import aio_pika

async def send_task(task_data):
    connection = await aio_pika.connect_robust("amqp://user:password@localhost/")
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=task_data.encode()),
            routing_key="task_queue",
        )