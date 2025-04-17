from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import auth, oauth
from app.config import settings
from app import __VERSION__


app = FastAPI(
    title="Auth Service",
    version=__VERSION__,
    description="User authentication microservice with JWT and Oauth2.0",
)

# 前後端分離
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(oauth.router, prefix="/aoi/v1/oauth", tags=["oauth"])

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}
