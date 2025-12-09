import pandas as pd
import joblib

def predict(new_data):
    model = joblib.load("../models/model.pkl")
    df = pd.DataFrame([new_data])
    prediction = model.predict(df)
    return prediction[0]

if __name__ == "__main__":
    example = {
        "feature1": 10,
        "feature2": 4,
        "feature3": 20
    }
    print("Prédiction :", predict(example))
