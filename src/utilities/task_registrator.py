from src.utilities.constants import FUNCTIONS


def task(func):
	"""
	Decorator to register a function for execution.
	"""
	FUNCTIONS[func.__name__] = func
	return func
