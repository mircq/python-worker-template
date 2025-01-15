from src.consumers.rabbitmq import RabbitMQConsumer
from src.consumers.ray import RayConsumer
from src.utilities.logger import logger
from src.utilities.settings import SETTINGS
import src.tasks

logger.info(f"Broker type is {SETTINGS.BROKER_TYPE}")

match SETTINGS.BROKER_TYPE:

    case "rabbitmq":

        RabbitMQConsumer().consume()

    case "ray":

        RayConsumer().consume()

    case "pulsar":

        PulsarConsumer().consume()

    case _:
        pass