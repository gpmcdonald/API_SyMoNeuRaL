from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ui import router as ui_router

def create_app() -> FastAPI:
    app = FastAPI(title="SyMoNeuRaL - API", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(ui_router, prefix="/ui", tags=["ui"])
    return app

app = create_app()
