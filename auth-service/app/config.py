from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_pwd: str
    db_usr: str
    port: str
    #origin
    BACKEND_CORS_ORIGINS: list[str]

    # JWT token
    JWT_KEY: str
    refresh_secret_key: str
    JWT_ALGO: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    #Oauth2.0
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str = "http://localhost:8000/api/v1/oauth/google/callback"

    # internal env
    adminapikey: str
    SERVER: str

    class Config:
        env_file  = ".env"


settings = Settings()