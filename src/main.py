import uvicorn
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from src.config import settings
from src.presentation.api.v1.router import api_v1_router as routers



def _include_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def _include_router(app: FastAPI) -> None:
    app.include_router(routers)



def create_app() -> FastAPI:
    app = FastAPI()
    _include_middleware(app)
    _include_router(app)

    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", host=settings.HOST, port=settings.PORT)
