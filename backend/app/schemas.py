from pydantic import BaseModel
from typing import List, Optional


class BuildListItemCreate(BaseModel):
    part_id: int


class PartRead(BaseModel):
    id: int
    name: str
    brand: str
    category: str
    price: float
    image_url: Optional[str]
    vendor: str
    product_url: str
    compatibility_notes: str
    tags: List[str]


class BuildListResponse(BaseModel):
    items: list[dict]
    total_cost: float
