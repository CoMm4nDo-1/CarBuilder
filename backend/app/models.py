from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Car(Base):
    __tablename__='cars'
    id: Mapped[int]=mapped_column(primary_key=True)
    make: Mapped[str]=mapped_column(String(64)); model: Mapped[str]=mapped_column(String(64)); generation: Mapped[str]=mapped_column(String(32))
    year_start: Mapped[int]; year_end: Mapped[int]; engine: Mapped[str]=mapped_column(String(64)); drivetrain: Mapped[str]=mapped_column(String(32))
    body_style: Mapped[str]=mapped_column(String(32)); chassis_code: Mapped[str]=mapped_column(String(16)); notes: Mapped[str|None]=mapped_column(Text, nullable=True)

class PartCategory(Base):
    __tablename__='part_categories'
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(64)); slug: Mapped[str]=mapped_column(String(64), unique=True); description: Mapped[str|None]=mapped_column(Text, nullable=True)
    display_order: Mapped[int]=mapped_column(default=0)

class Vendor(Base):
    __tablename__='vendors'
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(120)); website_url: Mapped[str]=mapped_column(String(255)); logo_url: Mapped[str|None]=mapped_column(String(255),nullable=True)
    affiliate_base_url: Mapped[str|None]=mapped_column(String(255),nullable=True); affiliate_program_name: Mapped[str|None]=mapped_column(String(120),nullable=True)
    notes: Mapped[str|None]=mapped_column(Text,nullable=True); is_active: Mapped[bool]=mapped_column(default=True)

class Part(Base):
    __tablename__='parts'
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(160)); brand: Mapped[str]=mapped_column(String(120)); category_id: Mapped[int]=mapped_column(ForeignKey('part_categories.id'))
    description: Mapped[str|None]=mapped_column(Text,nullable=True); base_price: Mapped[float]=mapped_column(Float); current_price: Mapped[float]=mapped_column(Float)
    image_url: Mapped[str|None]=mapped_column(String(255),nullable=True); vendor_id: Mapped[int|None]=mapped_column(ForeignKey('vendors.id'),nullable=True)
    product_url: Mapped[str]=mapped_column(String(255)); affiliate_url: Mapped[str|None]=mapped_column(String(255),nullable=True); availability_status: Mapped[str]=mapped_column(String(32),default='in_stock')
    source: Mapped[str]=mapped_column(String(64),default='manual_seed'); source_part_id: Mapped[str|None]=mapped_column(String(128),nullable=True); raw_source_data: Mapped[dict|None]=mapped_column(JSON,nullable=True)
    compatibility_notes: Mapped[str|None]=mapped_column(Text,nullable=True); tags: Mapped[list]=mapped_column(JSON,default=list)
    is_featured: Mapped[bool]=mapped_column(Boolean,default=False); is_sponsored: Mapped[bool]=mapped_column(Boolean,default=False); sponsor_label: Mapped[str|None]=mapped_column(String(64),nullable=True)
    last_updated: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow); created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow); updated_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)

class PartCompatibility(Base):
    __tablename__='part_compatibilities'
    id: Mapped[int]=mapped_column(primary_key=True); part_id: Mapped[int]=mapped_column(ForeignKey('parts.id')); car_id: Mapped[int]=mapped_column(ForeignKey('cars.id'))
    compatibility_type: Mapped[str]=mapped_column(String(32)); notes: Mapped[str|None]=mapped_column(Text,nullable=True)

class Build(Base):
    __tablename__='builds'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int|None]=mapped_column(ForeignKey('users.id'),nullable=True); title: Mapped[str]=mapped_column(String(120))
    car_id: Mapped[int]=mapped_column(ForeignKey('cars.id')); description: Mapped[str|None]=mapped_column(Text,nullable=True); is_public: Mapped[bool]=mapped_column(default=False)
    share_slug: Mapped[str|None]=mapped_column(String(80), unique=True, nullable=True); total_price_cached: Mapped[float]=mapped_column(Float, default=0)
    created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow); updated_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)

class BuildItem(Base):
    __tablename__='build_items'
    id: Mapped[int]=mapped_column(primary_key=True); build_id: Mapped[int]=mapped_column(ForeignKey('builds.id')); part_id: Mapped[int]=mapped_column(ForeignKey('parts.id'))
    quantity: Mapped[int]=mapped_column(Integer,default=1); price_at_time_added: Mapped[float]=mapped_column(Float); notes: Mapped[str|None]=mapped_column(Text,nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)

class User(Base):
    __tablename__='users'
    id: Mapped[int]=mapped_column(primary_key=True); email: Mapped[str]=mapped_column(String(160), unique=True); username: Mapped[str|None]=mapped_column(String(80),nullable=True)
    hashed_password: Mapped[str|None]=mapped_column(String(255),nullable=True); stripe_customer_id: Mapped[str|None]=mapped_column(String(128),nullable=True)
    subscription_status: Mapped[str]=mapped_column(String(32), default='inactive'); plan: Mapped[str]=mapped_column(String(16), default='free'); created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)

class PriceHistory(Base):
    __tablename__='price_history'
    id: Mapped[int]=mapped_column(primary_key=True); part_id: Mapped[int]=mapped_column(ForeignKey('parts.id')); vendor_id: Mapped[int|None]=mapped_column(ForeignKey('vendors.id'),nullable=True)
    price: Mapped[float]=mapped_column(Float); availability_status: Mapped[str]=mapped_column(String(32)); recorded_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)

class SponsoredPlacement(Base):
    __tablename__='sponsored_placements'
    id: Mapped[int]=mapped_column(primary_key=True); part_id: Mapped[int]=mapped_column(ForeignKey('parts.id')); vendor_id: Mapped[int|None]=mapped_column(ForeignKey('vendors.id'),nullable=True)
    placement_type: Mapped[str]=mapped_column(String(32)); starts_at: Mapped[datetime]=mapped_column(DateTime); ends_at: Mapped[datetime]=mapped_column(DateTime)
    is_active: Mapped[bool]=mapped_column(default=True); amount_paid: Mapped[float|None]=mapped_column(Float,nullable=True); stripe_payment_id: Mapped[str|None]=mapped_column(String(128),nullable=True)

class Payment(Base):
    __tablename__='payments'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int|None]=mapped_column(ForeignKey('users.id'),nullable=True)
    stripe_payment_intent_id: Mapped[str|None]=mapped_column(String(128),nullable=True); stripe_subscription_id: Mapped[str|None]=mapped_column(String(128),nullable=True)
    amount: Mapped[float]=mapped_column(Float); currency: Mapped[str]=mapped_column(String(8), default='usd'); status: Mapped[str]=mapped_column(String(32), default='created')
    payment_type: Mapped[str]=mapped_column(String(32)); created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
