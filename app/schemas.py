from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from app.database.db_models import NearestEarthObject

class ErrorSchema(BaseModel):
    """Define como uma mensagem de erro deve ser retornada."""

    mensagem: str

class NearestEarthObjectInfo(BaseModel):
    name: str
    est_diamenter_min: float
    est_diameter_max: float
    relative_velocity: float

    def check_if_neo_exists(self, session: Session) -> bool:
        """Verifica se um objeto próximo à Terra já existe no banco de dados."""
        neo = session.query(NearestEarthObject).filter(NearestEarthObject.name == self.name).first()
        return neo is not None

    def insert_neo_to_db(self, session: Session, hazardous: bool) -> NearestEarthObject:
        """Insere um objeto próximo à Terra no banco de dados."""
        try:
            if self.check_if_neo_exists(session):
                raise ValueError("O objeto próximo à Terra já existe no banco de dados.") 
            neo = NearestEarthObject(nearest_earth_object=self, hazardous=hazardous)
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
    message: str
    hazardous: bool

    @classmethod
    def from_neo_info(cls, neo_info: NearestEarthObjectInfo, hazardous: bool) -> "NearestEarthObjectInfoResponse":
        """Cria a resposta que será retornada na API."""
        message = f"O objeto {neo_info.name} foi inserido em nossa base de dados com sucesso. Periculosidade: {'Sim' if hazardous else 'Não'}."
        return cls(name=neo_info.name, message=message, hazardous=hazardous)



    