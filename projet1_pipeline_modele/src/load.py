""" Charger le modèle et produire un fichier de prédiction"""

import pandas as pd
import joblib

def generate_predictions():
    df = pd.read_csv("../data/processed/housing_clean.csv")
    model = joblib.load("../models/model.pkl")

    X = df.drop("target", axis=1)
    df["prediction"] = model.predict(X)

    df.to_csv("../data/final/predictions.csv", index=False)
    print("Prédictions générées dans data/final/predictions.csv")

if __name__ == "__main__":
    generate_predictions()
