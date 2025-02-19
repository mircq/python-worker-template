

class Serializer:

    @staticmethod
    def serialize(obj):
        if hasattr(obj, "__json__"):
            return obj.__json__()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")