from pydantic import BaseModel, PositiveFloat


class Edges(BaseModel):
    a: PositiveFloat
    b: PositiveFloat
    c: PositiveFloat


class BaseHeight(BaseModel):
    b: PositiveFloat
    h: PositiveFloat


class Area(BaseModel):
    area: float


class Perimetro(BaseModel):
    perimetro: float
