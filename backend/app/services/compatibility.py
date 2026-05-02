from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models import Part, PartCompatibility, PartCategory

def compatible_parts_query(db: Session, car_id: int, category_slug: str | None = None):
    q = select(Part).join(PartCompatibility, PartCompatibility.part_id==Part.id).where(PartCompatibility.car_id==car_id, PartCompatibility.compatibility_type.in_(['exact_fit','verify_fitment']))
    if category_slug:
        q = q.join(PartCategory, PartCategory.id==Part.category_id).where(PartCategory.slug==category_slug)
    return q
