from fastapi import FastAPI, HTTPException
from app.schemas import ErrorSchema, NearestEarthObjectInfo, NearestEarthObjectInfoResponse
from app.database import session
from app.ml_predict import predict_hazardous

app = FastAPI()

@app.post("/neo", responses={
    200: {"description": "Successful Response", "model": NearestEarthObjectInfoResponse},
    400: {"description": "Error Response", "model": ErrorSchema}
})
def create_nearest_earth_object(neo_info: NearestEarthObjectInfo):
    try:
        hazardous = predict_hazardous(neo_info)
        neo = neo_info.insert_neo_to_db(session, hazardous)
        response = NearestEarthObjectInfoResponse.from_neo_info(neo_info, hazardous)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao inserir o objeto no banco de dados: {e}")


