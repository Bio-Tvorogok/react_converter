from faststream.rabbit import RabbitExchange, ExchangeType

from react_converter.settings import settings

exchange = RabbitExchange(
    settings.EXCHANGE, auto_delete=True, type=ExchangeType.TOPIC
)
