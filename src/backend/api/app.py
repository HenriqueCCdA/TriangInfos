from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.config import settings
from api.routers import router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS,
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


app.include_router(router)
