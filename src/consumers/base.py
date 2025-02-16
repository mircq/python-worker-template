
class BaseConsumer:
    """
    Abstract base class for consumers.
    """

    def consume(self):
        raise NotImplementedError("Subclasses must implement the `consume` method.")
