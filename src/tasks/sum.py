from time import sleep

from src.entities.sum_entity import SumEntity
from src.errors.generic_errors import GenericErrors
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

	a: int | None = kwargs.get("a", None)
	b: int | None = kwargs.get("b", None)

	if a is None or b is None:
		logger.error(msg="Input params not found")
		return Result.fail(error=GenericErrors.generic_error(details="Input params not found"))

	sum: int = a + b

	sleep(15)

	result: SumEntity = SumEntity(value=sum)

	logger.info(msg="End")

	return Result.ok(value=result)
