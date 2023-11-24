from pydantic import BaseModel


class Edges(BaseModel):
    a: float
    b: float
    c: float


class BaseHeight(BaseModel):
    b: float
    h: float


class Area(BaseModel):
    area: float


class Perimetro(BaseModel):
    perimetro: float
