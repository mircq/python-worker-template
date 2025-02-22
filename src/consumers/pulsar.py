import json
from typing import Callable

from src.consumers.base import BaseConsumer
import pulsar

from src.results.result import Result
from src.utilities.constants import ENCODING
from src.utilities.logger import logger
from src.utilities.parameters_extractor import MessageHandler
from src.utilities.settings import SETTINGS


class PulsarConsumer(BaseConsumer):

    def __init__(self):

        """

        """

        self.client = pulsar.Client(
            service_url=f"pulsar://{SETTINGS.BROKER_HOST}:{SETTINGS.BROKER_PORT}"
        )

        self.consumer = self.client.subscribe(
            topic=SETTINGS.BROKER_QUEUE,
            subscription_name="aa", # TODO
            consumer_type=pulsar.ConsumerType.Shared  # Allows multiple consumers
        )

    def consume(self) -> None:

        """

        :return:
        """

        logger.info(msg="Start")


        logger.info(msg=f"Waiting for tasks from Pulsar topic '{self.consumer.topic}'...")
        try:
            while True:
                message = self.consumer.receive(timeout_millis=1000)
                try:
                    logger.info(msg=f"New message received")

                    parsing_result: Result[tuple[Callable, str | None, list, dict]] = MessageHandler.parse_incoming_message(
                        message=message.data().decode(encoding=ENCODING)
                    )

                    if parsing_result.failed:

                        logger.error(msg="An error occurred while parsing the message")

                    else:

                        function, response_queue, args, kwargs = parsing_result.value

                        result = MessageHandler.execute_function(function, *args, **kwargs)

                        self.consumer.acknowledge(message=message)

                        if response_queue:

                            self.send_response(response_queue=response_queue, result=result)

                except Exception as e:
                    logger.info(msg=f"Error processing message: {e}")
                    self.consumer.negative_acknowledge(message)
        except KeyboardInterrupt:
            logger.info(msg="Stopping Pulsar consumer...")
        finally:
            self.consumer.close()
            self.client.close()


    def send_response(self, response_queue: str, result: any) -> None:

        """

        :param response_queue:
        :param result:
        :return:
        """

        logger.info(msg="Start")
        logger.debug(msg=f"Input params: response_queue={response_queue}")

        producer: pulsar.Producer = self.client.create_producer(topic=response_queue)
        producer.send(content=json.dumps(result).encode(encoding=ENCODING))
        producer.close()

        logger.info(msg="End")