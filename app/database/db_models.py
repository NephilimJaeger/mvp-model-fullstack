from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class NearestEarthObjectInfo:
    name: str
    est_diamenter_min: int
    est_diameter_max: int
    relative_velocity: int
    hazardous: bool

class NearestEarthObject(Base):
    __tablename__ = "nearest_earth_object"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    est_diamenter_min = Column(Integer)
    est_diameter_max = Column(Integer)
    relative_velocity = Column(Integer)
    hazardous = Column(Boolean)


    def __init__(self, nearest_earth_object: NearestEarthObjectInfo):
        self.name = nearest_earth_object.name
        self.est_diamenter_min = nearest_earth_object.est_diamenter_min
        self.est_diameter_max = nearest_earth_object.est_diameter_max
        self.relative_velocity = nearest_earth_object.relative_velocity
        self.hazardous = nearest_earth_object.hazardous