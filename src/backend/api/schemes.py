from pydantic import BaseModel


class Edges(BaseModel):
    a: float
    b: float
    c: float


class Area(BaseModel):
    area: float
