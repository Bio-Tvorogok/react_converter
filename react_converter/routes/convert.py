from faststream.rabbit import RabbitRouter

from react_converter.config.rmq import exchange
from react_converter.settings import settings

router = RabbitRouter(prefix=f"{settings.SERVICE_NAME}.convert.")


@router.subscriber("in", exchange)
@router.publisher(routing_key="build_status", exchange=exchange)
async def convert(body) -> str:
    return body
