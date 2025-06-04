from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    #origin
    BACKEND_CORS_ORIGINS: list[str]

    #redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    


    # JWT token
    JWT_KEY: str
    # refresh_secret_key: str
    JWT_ALGO: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # REFRESH_TOKEN_EXPIRE_MINUTES: int

    #Oauth2.0
    # GOOGLE_CLIENT_ID: str
    # GOOGLE_CLIENT_SECRET: str
    # GOOGLE_REDIRECT_URI: str = "http://localhost:8000/api/v1/oauth/google/callback"


    class Config:
        env_file  = ".env"


settings = Settings()