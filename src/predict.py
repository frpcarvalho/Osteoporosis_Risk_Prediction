import joblib
import pandas as pd
import numpy as np

def load_model(model_path="models/stacking_ensemble_model.joblib"):
    return joblib.load(model_path)

def predict_osteoporosis_risk(data):
    model = load_model()
    return model.predict(data), model.predict_proba(data)
