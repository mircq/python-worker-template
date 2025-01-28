from src.utilities.constants import TASKS


def task(func):
	"""
	Decorator to register a function for execution.
	"""
	TASKS[func.__name__] = func
	return func
