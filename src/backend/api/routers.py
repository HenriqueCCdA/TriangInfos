from fastapi import APIRouter, HTTPException, status

from api.schemes import Area, BaseHeight, Edges, Perimetro
from api.services import Triang3Edges, TriangBaseHeight

router = APIRouter()


@router.get("/")
def index():
    return {"msg": "Api is OK!"}


@router.post("/area-abc", response_model=Area)
def calc_abc(edges: Edges):
    """Cálculo da area do triangulo utilizando os lados `a`, `b` e `c`."""

    triang = Triang3Edges(**edges.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "msg": "There is no triangle with these sides.",
                "type": "invalid_triangle",
                "input": edges.model_dump(),
            },
        )

    return {"area": triang.area()}


@router.post("/area-bh", response_model=Area)
def calc_bh(bh: BaseHeight):
    """Cálculo da área do triangulo com a `base` e a `altura`."""
    triang = TriangBaseHeight(**bh.model_dump())

    return {"area": triang.area()}


@router.post("/perimetro", response_model=Perimetro)
def perimetro(edges: Edges):
    """Cálculo da area do triangulo utilizando os lados `a`, `b` e `c`."""
    triang = Triang3Edges(**edges.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "msg": "There is no triangle with these sides.",
                "type": "invalid_triangle",
                "input": edges.model_dump(),
            },
        )

    return {"perimetro": triang.perimetro()}
