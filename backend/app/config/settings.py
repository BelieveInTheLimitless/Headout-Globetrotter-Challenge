import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Globetrotter API"
    MONGO_URI: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = "globetrotter"
    ORIGINS: list = [
        "https://your-frontend-deployment-url.up.railway.app",
        "http://localhost:5173"
    ]

    class Config:
        env_file = ".env"

settings = Settings()