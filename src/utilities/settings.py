from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	PORT: int = Field(title="PORT", description="Port on which the microservice is exposed.", default=8000)

	LOG_LEVEL: Literal["debug", "info", "warning", "error"] = Field(
		title="LOG_LEVEL", description="Level for log display.", default="info"
	)

	BROKER_TYPE: str = Field()

	BROKER_HOST: str = Field()

	BROKER_PORT: int = Field()

	BROKER_QUEUE: str = Field()


SETTINGS = Settings(_env_file=".env", _env_file_encoding="utf-8")
