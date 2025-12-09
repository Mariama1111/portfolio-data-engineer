import pandas as pd
import joblib

def predict(new_data):
    model = joblib.load("../models/model.pkl")
    df = pd.DataFrame([new_data])
    prediction = model.predict(df)
    return prediction[0]

if __name__ == "__main__":
   example = {"crim":0.1, "zn":18.0, "indus":2.3, "chas":0, "nox":0.4, "rm":6.0, 
              "age":65.0, "dis":4.0, "rad":1, "tax":300, "ptratio":15, "b":390, "lstat":5}
    pred = predict(example)
    print(f"Prédiction pour l'exemple : {pred:.3f}")
