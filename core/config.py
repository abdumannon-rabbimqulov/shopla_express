import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://shopla_user:shopla_password@localhost:5432/shopla_db")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_change_me_in_production")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # SMTP Settings
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.resend.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
    SMTP_SECURE = os.getenv("SMTP_SECURE", "true").lower() == "true"
    SMTP_USER = os.getenv("SMTP_USER", "resend")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "re_X9tYuZDa_FcHqpdhbXApb9s4MBhi5Nwxh")
    SMTP_FROM = os.getenv("SMTP_FROM", "Shopla <noreply@shopla.uz>")

settings = Settings()
