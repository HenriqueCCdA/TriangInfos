from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from api.schemes import Area, Edges
from api.services import Triang

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


@app.post("/area", response_model=Area)
def calc(edges: Edges):
    triang = Triang(**edges.model_dump())

    if not triang.is_valid():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Não existe triangulo com esse lados."
        )

    return {"area": triang.area()}
