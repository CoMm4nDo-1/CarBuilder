from sqlmodel import SQLModel, create_engine, Session, select
from .models import Car, PartCategory, Part, BuildListItem

engine = create_engine('sqlite:///./carbuilder.db', echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def seed_data(session: Session):
    if session.exec(select(Car)).first():
        return
    car = Car(make='BMW', model='328i', generation='E90', year_start=2006, year_end=2011, engine='N52')
    session.add(car)
    categories = ['Suspension', 'Intake', 'Exhaust', 'Wheels', 'Tune', 'Brakes', 'Exterior', 'Interior']
    for c in categories:
        session.add(PartCategory(name=c))
    parts = [
        ('BC Racing BR Series Coilovers','BC Racing','Suspension',1195,'Example Vendor','https://example.com/bc-racing-e90-328i','Fits BMW E90 328i RWD models. Verify fitment for xDrive.','E90,328i,RWD,Suspension'),
        ('Bilstein B12 Pro-Kit','Bilstein','Suspension',1099,'Turner Motorsport','https://example.com/bilstein-b12-e90','Matched dampers and springs for street use.','E90,328i,Suspension,Street'),
        ('Megan Racing Front Strut Bar','Megan Racing','Suspension',179,'ECS Tuning','https://example.com/megan-strut-e90','Front brace for improved rigidity.','E90,Chassis,Suspension'),
        ('aFe Magnum FORCE Intake','aFe','Intake',399,'FCP Euro','https://example.com/afe-intake-e90','N52 compatible cold-air intake.','E90,328i,N52,Intake'),
        ('Injen SP Intake','Injen','Intake',349,'ModBargains','https://example.com/injen-sp-e90','Improved airflow and intake sound.','E90,328i,N52,Intake'),
        ('K&N Drop-in Filter','K&N','Intake',69,'Amazon','https://example.com/kn-filter-e90','Stock airbox replacement filter.','E90,328i,N52,Budget'),
        ('Supersprint Axle-Back','Supersprint','Exhaust',899,'Vivid Racing','https://example.com/supersprint-e90','Sportier tone with OEM-like fit.','E90,328i,Exhaust'),
        ('Borla Cat-Back System','Borla','Exhaust',1249,'Borla Dealer','https://example.com/borla-e90','Stainless cat-back exhaust system.','E90,328i,Exhaust,Performance'),
        ('Muffler Delete Pipe Kit','Rev9','Exhaust',249,'eBay','https://example.com/rev9-delete-e90','Louder setup; check local regulations.','E90,Exhaust,Budget'),
        ('Apex ARC-8 18x9','Apex','Wheels',1480,'Apex Wheels','https://example.com/apex-arc8-e90','Square setup for balanced grip.','E90,Wheels,Track'),
        ('Enkei TS-5 18x8.5','Enkei','Wheels',1180,'Tire Rack','https://example.com/enkei-ts5-e90','Lightweight wheel option.','E90,Wheels,Street'),
        ('BBS SR 18x8','BBS','Wheels',1599,'BBS USA','https://example.com/bbs-sr-e90','Premium flow-formed wheel.','E90,Wheels,Premium'),
        ('BMS Power Box','Burger Motorsports','Tune',289,'BMS','https://example.com/bms-powerbox-n52','Piggyback tune for N52 applications.','N52,Tune,328i'),
        ('AA Performance Tune','Active Autowerke','Tune',499,'AA','https://example.com/aa-tune-e90','ECU tune optimized for bolt-ons.','E90,N52,Tune'),
        ('Dinan Stage 1 Software','Dinan','Tune',599,'Dinan','https://example.com/dinan-stage1-e90','Conservative tune with drivability focus.','E90,N52,Tune,Street'),
        ('StopTech Sport Pads','StopTech','Brakes',189,'RockAuto','https://example.com/stoptech-pads-e90','Street/spirited driving brake pads.','E90,Brakes,Street'),
        ('EBC Yellowstuff Pads','EBC','Brakes',209,'FCP Euro','https://example.com/ebc-yellow-e90','Aggressive pad for occasional track use.','E90,Brakes,Track'),
        ('Zimmermann Rotor Set','Zimmermann','Brakes',329,'ECS Tuning','https://example.com/zimmermann-e90','OEM-style drilled rotor replacement.','E90,Brakes,OEM+'),
        ('M Sport Front Bumper','BMW','Exterior',749,'BMW Parts','https://example.com/msport-bumper-e90','Requires paint and trim transfer.','E90,Exterior,OEM'),
        ('Carbon Fiber Trunk Lip','RW Carbon','Exterior',229,'RW Carbon','https://example.com/trunk-lip-e90','Simple adhesive trunk lip spoiler.','E90,Exterior,Style'),
        ('Black Kidney Grilles','IND','Exterior',129,'IND Distribution','https://example.com/kidney-black-e90','Gloss black grille set.','E90,Exterior,Budget'),
        ('M3 Style Side Skirts','Duraflex','Exterior',419,'CarID','https://example.com/side-skirt-e90','Aftermarket side skirt kit.','E90,Exterior,Body'),
        ('LED Angel Eye Kit','Lux','Exterior',169,'Lux H8','https://example.com/lux-angel-e90','Brighter halo lighting conversion.','E90,Exterior,Lighting'),
        ('Short Shift Kit','Rogue Engineering','Interior',395,'Turner Motorsport','https://example.com/ssk-e90','Shorter throw for 6MT cars.','E90,Interior,6MT'),
        ('Alcantara Shift Boot','Macht Schnell','Interior',89,'ModAuto','https://example.com/alcantara-boot-e90','Interior refresh for shift area.','E90,Interior,Style'),
        ('M Sport Steering Wheel','BMW','Interior',699,'BMW Parts','https://example.com/msport-wheel-e90','Direct replacement wheel.','E90,Interior,OEM'),
        ('All-Weather Floor Mats','WeatherTech','Interior',149,'WeatherTech','https://example.com/floormats-e90','Laser-fit floor protection.','E90,Interior,Daily'),
        ('Android Head Unit','Avin','Interior',629,'Avin USA','https://example.com/avin-headunit-e90','CarPlay/Android Auto upgrade.','E90,Interior,Tech'),
        ('H&R Sport Springs','H&R','Suspension',299,'FCP Euro','https://example.com/hr-springs-e90','Lowering springs for stock dampers.','E90,328i,Suspension'),
        ('AFE Exhaust Midpipe','aFe','Exhaust',599,'aFe Power','https://example.com/afe-midpipe-e90','Freer-flowing midpipe section.','E90,328i,Exhaust')
    ]
    for p in parts:
        session.add(Part(name=p[0],brand=p[1],category=p[2],price=p[3],vendor=p[4],product_url=p[5],compatibility_notes=p[6],tags=p[7]))
    session.commit()


def init_db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed_data(session)
