import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def prepare_data(data, target_cols):
    X = data.drop(columns=target_cols, errors='ignore')
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = pd.to_numeric(X[col], errors='coerce')
    return X
