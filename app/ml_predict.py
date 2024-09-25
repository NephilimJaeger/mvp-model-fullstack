from pickle import load
from app.database.db_models import NearestEarthObjectInfo


def predict_hazardous(neo_info: NearestEarthObjectInfo) -> bool:
    """Realiza a predição de periculosidade de um objeto celeste."""
    
    with open('data/pipeline.pkl', 'rb') as file:
        pipeline = load(file)
    data = [[neo_info.est_diamenter_min, neo_info.relative_velocity]]
    prediction = pipeline.predict(data)

    return bool(prediction)