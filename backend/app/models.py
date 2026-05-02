from __future__ import annotations

from typing import Optional
from sqlmodel import SQLModel, Field


class Car(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    make: str
    model: str
    generation: str
    year_start: int
    year_end: int
    engine: str


class PartCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Part(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    brand: str
    category: str
    price: float
    image_url: Optional[str] = None
    vendor: str
    product_url: str
    compatibility_notes: str
    tags: str


class BuildListItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    part_id: int
