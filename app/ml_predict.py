import joblib
from app.database.db_models import NearestEarthObjectInfo

# Carregar o modelo de machine learning
# model = joblib.load("path/to/your/model.pkl")

def predict_hazardous(neo_info: NearestEarthObjectInfo) -> bool:
    # Prepare os dados para a predição
    # data = [[neo_info.est_diamenter_min, neo_info.est_diameter_max, neo_info.relative_velocity]]
    # # Rodar a predição
    # prediction = model.predict(data)
    prediction = [0,1]
    # Retornar se é perigoso ou não
    return bool(prediction[0])