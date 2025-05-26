from fastapi import FastAPI
from app import __VERSION__
from app.routers import asset

app = FastAPI(
    title="Asset Service",
    version=__VERSION__,
    description="Asset recording service"
)

app.include_router(asset.router)