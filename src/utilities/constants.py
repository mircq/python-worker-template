from typing import Literal, Callable

LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
FUNCTIONS: dict[str, Callable] = {}
BROKER_TYPE = Literal["rabbitmq"]
