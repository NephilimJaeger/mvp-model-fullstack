from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from dataclasses import dataclass
from models import Base

@dataclass
class AvaliacaoBase:
    id: int
    flight_distance: int
    inflight_wifi_service: int
    food_and_drink: int
    online_boarding: int
    seat_comfort: int
    inflight_entertainment: int
    onboard_service: int
    leg_room_service: int
    baggage_handling: int
    checkin_service: int
    inflight_service: int
    cleanliness: int
    travel_type: str
    travel_class: str
    satisfaction: str


class Avaliacao(Base):
    __tablename__ = "avaliacao"

    id = Column(Integer, primary_key=True)
    flight_distance = Column(Integer)
    inflight_wifi_service = Column(Integer)
    food_and_drink = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    inflight_entertainment = Column(Integer)
    onboard_service = Column(Integer)
    leg_room_service = Column(Integer)
    baggage_handling = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)
    travel_type = Column(String)
    travel_class = Column(String)
    satisfaction = Column(String)

    def __init__(self, avaliacao: AvaliacaoBase):
        self.id = avaliacao.id
        self.gender = avaliacao.gender
        self.flight_distance = avaliacao.flight_distance
        self.inflight_wifi_service = avaliacao.inflight_wifi_service
        self.food_and_drink = avaliacao.food_and_drink
        self.online_boarding = avaliacao.online_boarding
        self.seat_comfort = avaliacao.seat_comfort
        self.inflight_entertainment = avaliacao.inflight_entertainment
        self.onboard_service = avaliacao.onboard_service
        self.leg_room_service = avaliacao.leg_room_service
        self.baggage_handling = avaliacao.baggage_handling
        self.checkin_service = avaliacao.checkin_service
        self.inflight_service = avaliacao.inflight_service
        self.cleanliness = avaliacao.cleanliness
        self.type_of_travel = avaliacao.type_of_travel
        self.travel_class = avaliacao
        self.satisfaction = avaliacao.satisfaction
