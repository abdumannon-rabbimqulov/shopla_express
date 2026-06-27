import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://shopla_user:shopla_password@localhost:5432/shopla_db")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_change_me_in_production")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

settings = Settings()
