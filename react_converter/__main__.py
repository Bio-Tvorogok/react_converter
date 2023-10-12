import asyncio

from react_converter.app import create_app
from react_converter.utils.logging_loader import init_logging

if __name__ == "__main__":
    init_logging()
    asyncio.run(create_app())
