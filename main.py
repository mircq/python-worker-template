from typing import get_args

from src.consumers.pulsar import PulsarConsumer
from src.consumers.rabbitmq import RabbitMQConsumer
from src.consumers.ray import RayConsumer
from src.utilities.constants import BROKER_TYPE, TASKS
from src.utilities.logger import logger
from src.utilities.settings import SETTINGS
import src.tasks    # Do not remove: it register tasks

logger.info(msg=f"Registered tasks: {'\n\u2022'.join(list(TASKS.keys()))}")

logger.info(msg=f"Broker type is {SETTINGS.BROKER_TYPE}")

match SETTINGS.BROKER_TYPE:

    case "rabbitmq":

        RabbitMQConsumer().consume()

    case "ray":

        RayConsumer().consume()

    case "pulsar":

        PulsarConsumer().consume()

    case _:
        logger.error(msg=f"Broker type {SETTINGS.BROKER_TYPE} not supported. Currently supported brokers: {list(get_args(BROKER_TYPE))}")
        pass