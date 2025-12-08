""" Script de suppression de lignes vides, renomme la colonne cible, normalise et sauvegarde des données transfomées"""

import pandas as pd

def transform_data(df):
  # Supprimer les lignes avec valeurs manquantes
  df = df.dropna()
  
  # renommer une colonne
  df = df.rename(columns={"medv" : "target"})
  
  # exemple de transformation simple : normaliser la colonne target
  df["target"] = (df["target"].mean()) / df["target"].std()
  
  return df

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/housing.csv")
    df_clean = transform_data(df)
    df_clean.to_csv("../data/processed/housing_clean.csv", index=False)
    print("Données transformées et sauvegardées !")
