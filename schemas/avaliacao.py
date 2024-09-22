from pydantic import BaseModel
from models import Avaliacao
from sqlalchemy.orm.session import Session

class AvaliacaoBase(BaseModel):
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
    type_of_travel: str
    travel_class: str
    satisfaction: str

class AvaliacaoDisplay:
    msg: str


def salvar_avaliacao(avaliacao: AvaliacaoBase, session: Session):
    avaliacao = Avaliacao(avaliacao)
    session.add(avaliacao)
    session.commit()
    session.refresh(avaliacao)
    return avaliacao
    
    