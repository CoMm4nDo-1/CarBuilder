from pydantic import BaseModel
import os

class Settings(BaseModel):
    database_url: str = os.getenv('DATABASE_URL', 'sqlite:///./carparts.db')
    frontend_url: str = os.getenv('FRONTEND_URL', 'http://localhost:3000')
    stripe_secret_key: str = os.getenv('STRIPE_SECRET_KEY', '')
    stripe_webhook_secret: str = os.getenv('STRIPE_WEBHOOK_SECRET', '')
    stripe_premium_price_id: str = os.getenv('STRIPE_PREMIUM_PRICE_ID', '')

settings = Settings()
