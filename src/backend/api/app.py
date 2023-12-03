from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.config import settings
from api.schemes import Area, BaseHeight, Edges, Perimetro
from api.services import Triang3Edges, TriangBaseHeight

app = FastAPI()

origins = settings.CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exeception_handler(request: Request, exec: RequestValidationError):
    new_errors = [
        {
            "type": e["type"],
            "msg": e["msg"],
            "input": e["input"],
            "loc": e["loc"],
        }
        for e in exec.errors()
    ]
    return JSONResponse({"detail": new_errors}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
def index():
    return {"msg": "Api is OK!"}


@app.post("/area-abc", response_model=Area)
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


@app.post("/area-bh", response_model=Area)
def calc_bh(bh: BaseHeight):
    """Cálculo da área do triangulo com a `base` e a `altura`."""
    triang = TriangBaseHeight(**bh.model_dump())

    return {"area": triang.area()}


@app.post("/perimetro", response_model=Perimetro)
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
