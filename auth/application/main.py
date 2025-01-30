from contextlib import asynccontextmanager

from application.api.v1.handlers.auth import router as auth_router
from application.core.config import get_settings
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    pass


app = FastAPI(
    title=get_settings().app.project_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    # lifespan=lifespan,
)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/api/docs")


app.include_router(auth_router, prefix="/auth", tags=["auth"])
