# app/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict  # imports the Pydantic Settings base & config
from pydantic import AnyUrl, Field  # types & defaults for validation

class Settings(BaseSettings):  # a class that reads env vars into typed fields
    model_config = SettingsConfigDict(
        env_file=".env",                 # <-- tells Pydantic to load src/aetherops-api/.env
        env_file_encoding="utf-8",       # <-- read the file as UTF-8
        extra="ignore"                   # <-- ignore unknown env keys, keeps things tolerant
    )

    DATABASE_URL: str = Field(..., description="SQLAlchemy URL, e.g., postgresql://... or sqlite+aiosqlite:///...")  
    ENV: str = Field("dev", description="Runtime environment name")

# instance to import elsewhere
settings = Settings()  # <-- reads .env at import time
