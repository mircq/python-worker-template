import ray

from src.consumers.base import ConsumerBase
from src.utilities.settings import SETTINGS


class RayConsumer(ConsumerBase):
	"""
	Ray-based task consumer.
	"""

	def __init__(self):
		ray.init(address=f"ray://{SETTINGS.BROKER_HOST}:{SETTINGS.BROKER_PORT}")

	def consume(self):
		"""
		Ray consumer does not explicitly consume tasks.
		Tasks are executed dynamically when submitted in Ray.
		"""
		print("Ray does not require a consumer process. Tasks are automatically scheduled.")
		# Optionally implement any custom behavior if necessary (e.g., logs, metrics).
