from src.results.result import Result
from src.utilities.logger import logger
from src.utilities.task_registrator import task


@task
def template_task(*args, **kwargs):
	"""

	:return:
	"""

	logger.info(msg="Start")
	logger.debug(msg=f"Input params: args={args}, kwargs={kwargs}")

	result = 21

	logger.info(msg="End")

	return Result.ok(value=result)
