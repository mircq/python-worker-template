from typing import Literal, Callable

LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
TASKS: dict[str, Callable] = {}
BROKER_TYPE = Literal["rabbitmq"]
ENCODING = Literal["utf-8"]
