import pandas as pd
import pytest
from pickle import load
from sklearn.metrics import accuracy_score, recall_score

ACCURACY = 0.8
RECALL = 0.5

path_pipeline = "data/pipeline.pkl"
path_data_tests = "data/neo_to_tests.csv"

@pytest.fixture
def pipeline():
    with open(path_pipeline, "rb") as file:
        return load(file)

@pytest.fixture(scope="module")
def test_data():
    data = pd.read_csv(path_data_tests)
    X, y = data.drop("hazardous", axis=1), data["hazardous"]
    return X, y

def test_model_accuracy(pipeline, test_data):
    X, y = test_data
    y_pred = pipeline.predict(X)
    accuracy = accuracy_score(y, y_pred)
    assert accuracy >= ACCURACY, f"Expected accuracy >= {ACCURACY}, but got {accuracy}"


def test_model_recall(pipeline, test_data):
    X, y = test_data
    y_pred = pipeline.predict(X)
    recall = recall_score(y, y_pred)
    assert recall >= RECALL, f"Expected recall >= {RECALL}, but got {recall}"
        


