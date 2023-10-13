from pathlib import Path

from pydantic import AmqpDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Rabbit
    RMQ_URL: AmqpDsn
    EXCHANGE: str = "services"

    # Service env
    SERVICE_NAME: str = "react"
    DEBUG: bool
    TEMPLATE: Path = Path("./template.tar.gz")

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
