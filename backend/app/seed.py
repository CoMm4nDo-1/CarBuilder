from sqlalchemy import select
from .database import Base, engine, SessionLocal
from .models import Car, PartCategory, Vendor, Part, PartCompatibility

CATS=[('Suspension','suspension'),('Intake','intake'),('Exhaust','exhaust'),('Wheels','wheels'),('Tune','tune'),('Brakes','brakes'),('Exterior','exterior'),('Interior','interior'),('Cooling','cooling'),('Maintenance','maintenance')]
PARTS=['BC Racing BR Series Coilovers','KW V1 Coilovers','Bilstein B12 Suspension Kit','H&R Sport Springs','AFE Power Intake','K&N Intake Kit','MagnaFlow Cat-Back Exhaust','Supersprint Exhaust','Apex ARC-8 Wheels','Enkei RPF1 Wheels','StopTech Brake Kit','Hawk Performance Pads','Turner Motorsport Tune','Burger Motorsports Tune Module','M Sport Front Bumper','Carbon Fiber Spoiler','Short Shift Kit','Cooling Refresh Kit','CSF Aluminum Radiator','Mishimoto Expansion Tank','M3 Control Arms','Megan Strut Bar','Injen Intake','Borla Catback','BBS SR Wheels','EBC Yellow Pads','Zimmerman Rotors','Black Kidney Grilles','All Weather Mats','Android Headunit']

def run_seed():
    Base.metadata.create_all(engine)
    db=SessionLocal()
    if db.scalar(select(Car.id)): return
    car=Car(make='BMW',model='328i',generation='E90',year_start=2006,year_end=2011,engine='N52',drivetrain='RWD',body_style='Sedan',chassis_code='E90',notes='MVP base car')
    db.add(car); db.flush()
    cmap={}
    for i,(n,s) in enumerate(CATS): c=PartCategory(name=n,slug=s,display_order=i);db.add(c);db.flush();cmap[n]=c.id
    vendor=Vendor(name='Example Vendor Network',website_url='https://example.com',affiliate_program_name='Demo Affiliate',is_active=True);db.add(vendor);db.flush()
    for i,name in enumerate(PARTS):
        cat=CATS[i%len(CATS)][0]
        p=Part(name=name,brand=name.split()[0],category_id=cmap[cat],description=f'{name} for BMW E90 328i',base_price=199+i*25,current_price=219+i*25,image_url='https://images.unsplash.com/photo-1487754180451-c456f719a1fc?w=800',vendor_id=vendor.id,product_url=f'https://example.com/parts/{i+1}',affiliate_url=f'https://example.com/aff/parts/{i+1}',availability_status='in_stock',source='manual_seed',source_part_id=f'MAN-{i+1}',raw_source_data={'seed':True},compatibility_notes='Fits BMW E90 328i N52; verify xDrive fitment.',tags=['E90','328i','N52',cat],is_featured=i%7==0,is_sponsored=i%11==0,sponsor_label='Sponsored' if i%11==0 else None)
        db.add(p); db.flush(); db.add(PartCompatibility(part_id=p.id,car_id=car.id,compatibility_type='exact_fit',notes='Seed rule'))
    db.commit(); db.close()

if __name__=='__main__': run_seed()
