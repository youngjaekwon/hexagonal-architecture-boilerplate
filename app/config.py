from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "sqlite:///sqlite3.db"
    ENV: str = "dev"


def get_settings():
    return Settings()
