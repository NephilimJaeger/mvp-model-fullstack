from pickle import load
from backend.database.db_models import NearestEarthObjectInfo

MODEL_PATH = "data/pipeline.pkl"

def predict_hazardous(neo_info: NearestEarthObjectInfo) -> bool:
    """Realiza a predição de periculosidade de um objeto celeste."""

    with open(MODEL_PATH, "rb") as file:
        pipeline = load(file)
    data = [[neo_info.est_diameter_max, neo_info.relative_velocity, neo_info.absolute_magnitude]]
    prediction = pipeline.predict(data)

    return bool(prediction)
