from pydantic import BaseModel, Field


class SumEntity(BaseModel):

    """

    """

    value: int = Field()

    def __json__(self):

        return self.model_dump()