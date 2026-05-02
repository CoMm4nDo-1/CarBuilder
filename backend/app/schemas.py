from pydantic import BaseModel
from typing import Optional

class BuildItemCreate(BaseModel):
    part_id: int
    quantity: int = 1

class BuildCreate(BaseModel):
    title: str
    car_id: int
    description: Optional[str] = None

class PaymentSessionRequest(BaseModel):
    amount: int = 0
    currency: str = 'usd'
