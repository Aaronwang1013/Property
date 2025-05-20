from fastapi import FastAPI, HTTPException
from app.api.routes import router as property
from app import __VERSION__

app = FastAPI(
    title="Property track",
    version=__VERSION__
)

app.include_router(property, prefix="/api/v1/property")