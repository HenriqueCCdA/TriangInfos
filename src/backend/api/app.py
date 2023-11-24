from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from api.schemes import Area, BaseHeight, Edges, Perimetro
from api.services import Triang3Edges, TriangBaseHeight

app = FastAPI()


origins = ["http://localhost:5173", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"msg": "Api is OK!"}


@app.post("/area-abc", response_model=Area)
def calc_abc(edges: Edges):
    """Cálculo da area do triangulo utilizando os lados `a`, `b` e `c`."""
    triang = Triang3Edges(**edges.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Não existe triangulo com esse lados."
        )

    return {"area": triang.area()}


@app.post("/area-bh", response_model=Area)
def calc_bh(bh: BaseHeight):
    """Cálculo da área do triangulo com a `base` e a `altura`."""
    triang = TriangBaseHeight(**bh.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Não existe triangulo com esse lados."
        )

    return {"area": triang.area()}


@app.post("/perimetro", response_model=Perimetro)
def perimetro(edges: Edges):
    """Cálculo da area do triangulo utilizando os lados `a`, `b` e `c`."""
    triang = Triang3Edges(**edges.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Não existe triangulo com esse lados."
        )

    return {"perimetro": triang.perimetro()}
