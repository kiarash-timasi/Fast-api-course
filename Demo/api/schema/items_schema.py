from typing import List
from pydantic import BaseModel, ConfigDict

class ItemModelCommand(BaseModel):
    id: int
    name: str
    city: str

class ItemResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    city: str


class ItemsResponseSchema(BaseModel):
    items: List[ItemResponseSchema]
