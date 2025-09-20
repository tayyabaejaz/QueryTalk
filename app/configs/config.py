from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    OLLAMA_MODEL: str = "llama3"

    class Config:
        env_file = ".env"   # tells Pydantic to read .env file

settings = Settings()
