import asyncio

from react_converter.app import create_app
from react_converter.storage import template_storage
from react_converter.utils.logging_loader import init_logging

if __name__ == "__main__":
    init_logging()
    template_storage.start_up()
    asyncio.run(create_app())
