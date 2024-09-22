from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from app.database.db_models import NearestEarthObject

class ErrorSchema(BaseModel):
    """Define como uma mensagem de erro deve ser retornada."""

    mensagem: str

class NearestEarthObjectInfo(BaseModel):
    name: str
    est_diamenter_min: int
    est_diameter_max: int
    relative_velocity: int
    hazardous: bool

    def insert_neo_to_db(self, session: Session):
        """Insere um objeto próximo à Terra no banco de dados."""
        try: 
            neo = NearestEarthObject(name=self.name, est_diamenter_min=self.est_diamenter_min,
                                 est_diameter_max=self.est_diameter_max, relative_velocity=self.relative_velocity,
                                 hazardous=self.hazardous)
            session.add(neo)
            session.commit()
            session.refresh(neo)
            return neo
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        
       
class NearestEarthObjectInfoResponse(BaseModel):
    """Define como um objeto de informação de um objeto próximo à Terra deve ser retornado."""
    name: str
    hazardous: bool

    @classmethod
    def from_neo_info(cls, neo_info: NearestEarthObjectInfo):
        """Cria a resposta que será retornada na API."""
        return cls(name=neo_info.name, hazardous=neo_info.hazardous)



    