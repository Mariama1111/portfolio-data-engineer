""" Vérification de l'efficacité du modèle"""

import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def validate_model():
    df = pd.read_csv("../data/processed/housing_clean.csv")
    model = joblib.load("../models/model.pkl")

    X = df.drop("target", axis=1)
    y = df["target"]

    preds = model.predict(X)
    accuracy = accuracy_score(y, preds)
    print("Accuracy :", accuracy)

if __name__ == "__main__":
    validate_model()
