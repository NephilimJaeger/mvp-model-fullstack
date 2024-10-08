from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Float
from dataclasses import dataclass

Base = declarative_base()


@dataclass
class NearestEarthObjectInfo:
    name: str
    est_diameter_max: int
    relative_velocity: int
    absolute_magnitude: float


class NearestEarthObject(Base):
    __tablename__ = "nearest_earth_object"

    name = Column(String, primary_key=True, unique=True)
    est_diameter_max = Column(Float)
    relative_velocity = Column(Float)
    absolute_magnitude = Column(Float)
    hazardous = Column(Boolean)

    def __init__(self, nearest_earth_object: NearestEarthObjectInfo, hazardous: bool):
        self.name = nearest_earth_object.name
        self.est_diameter_max = nearest_earth_object.est_diameter_max
        self.relative_velocity = nearest_earth_object.relative_velocity
        self.absolute_magnitude = nearest_earth_object.absolute_magnitude
        self.hazardous = hazardous
