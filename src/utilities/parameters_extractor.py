import json
from typing import Callable

from src.errors.generic_errors import GenericErrors
from src.results.result import Result
from src.utilities.constants import FUNCTIONS
from src.utilities.logger import logger

class MessageHandler:

    @staticmethod
    def parse_incoming_message(message: str) -> Result[tuple[Callable, str | None, list, dict]]:

        """

        :param str message:
        :return:
        """

        body: dict = json.loads(message)

        function_name = body.get("function_name", None)

        if function_name is None:
            return Result.fail(error=GenericErrors.missing_function_error())

        # Fetch the function from the mapping
        function: Callable | None = FUNCTIONS.get(function_name, None)

        if function is None:
            return Result.fail(error=GenericErrors.function_not_found_error(name=function.__name__))

        args = body.get("args", [])
        kwargs = body.get("kwargs", {})

        response_queue = body.get("response_queue", None)

        return Result.ok(value=(function, response_queue, args, kwargs))

    def execute_function(function: Callable, *args, **kwargs):
        """
        Execute a function based on the message content.
        The message must include 'function_name' and 'args'.

        :param message:
        """

        logger.info(msg="Start")

        try:

            # Call the function with args and kwargs
            result = function(*args, **kwargs)

            logger.info(msg="End")

            return result
        except Exception as e:
            return Result.fail(error=GenericErrors.generic_error(details=str(e)))