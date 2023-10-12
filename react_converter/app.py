from faststream import FastStream
from faststream.rabbit import RabbitBroker

from react_converter.routes import convert
from react_converter.settings import settings


async def create_app():
    broker = RabbitBroker(str(settings.RMQ_URL))
    broker.include_router(convert.router)
    app = FastStream(broker, title=settings.SERVICE_NAME.title())

    await FastStream.run(app)
