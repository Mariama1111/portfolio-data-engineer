import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    df = pd.read_csv("../data/processed/Housing_clean.csv")

    # selection 
    X = df.drop("target", axis=1)
    y = df["target"]

    # séparation jeu d'entraînement et jeu de test  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # création du modèle
    model = LogisticRegression()
  
    # entrainement du modèle
    model.fit(X_train, y_train)

    # sauvegarde du modèle .pkl proprement avec joblib
    joblib.dump(model, "../models/model.pkl")
    print("Modèle entraîné et sauvegardé !")

if __name__ == "__main__":
    train_model()

