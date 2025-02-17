from src.errors.error import Error

from src.utilities.logger import logger


class GenericErrors:
	"""Generic errors container"""

	@staticmethod
	def generic_error(details: str) -> Error:
		"""
		Creates a new generic error with details passed as parameter and 500 as status code.

		:param str details: error details.
		:return: an Error object with the given details.
		:rtype: Error
		"""
		logger.error(msg=f"A generic error occurred. Details: {details}")

		return Error(
			message=f"A generic error occurred. Details: {details}",
			status_code=500,
		)

	@staticmethod
	def function_not_found_error(name: str) -> Error:
		"""
		Creates a NotFound error with the given details and 404 as status code.

		:param str name: function name.
		:return: an Error object with the given details.
		:rtype: Error
		"""

		logger.error(msg=f"Function {name} not found, or not marked as task.")

		return Error(
			message=f"Function {name} not found, or not marked as task.",
			status_code=404,
		)

	@staticmethod
	def missing_function_error() -> Error:
		"""
		Creates a missing function error with 422 as status code.

		:return: an Error object with the given details.
		:rtype: Error
		"""

		logger.error(
			msg="No function provided. Please specify the function to be executed in the 'function_name' parameter."
		)

		return Error(
			message="No function provided. Please specify the function to be executed in the 'function_name' parameter.",
			status_code=422,
		)
