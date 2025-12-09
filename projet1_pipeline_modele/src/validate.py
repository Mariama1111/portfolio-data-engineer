""" Vérification de l'efficacité du modèle"""

import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import joblib

def validate_model():
    df = pd.read_csv("../data/processed/housing_clean.csv")
    model = joblib.load("../models/model.pkl")

    X = df.drop("target", axis=1)
    y = df["target"]

    preds = model.predict(X)
    r2 = r2_score(y, preds)
    mse = mean_squared_error(y, preds)

    print(f"R2 score: {r2:.3f}")
    print(f"MSE: {mse:.3f}")

if __name__ == "__main__":
    validate_model()
