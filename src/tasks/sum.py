from src.results.result import Result
from src.utilities.logger import logger
from src.utilities.task_registrator import task


@task
def sum(*args, **kwargs):
	"""

	:return:
	"""

	logger.info(msg="Start")
	logger.debug(msg=f"Input params: args={args}, kwargs={kwargs}")

	a: int = kwargs.get("a")
	b: int = kwargs.get("b")

	result = a + b

	logger.info(msg="End")

	return Result.ok(value=result)
