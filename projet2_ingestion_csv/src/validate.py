""" vérifier les colonnes / vérifier si il y a des valeurs manquantes / voir les statistiques """

import pandas as pd

def validate_data():
    df = pd.read_csv("../data/processed/sales_clean.csv")

    print("Aperçu des données :")
    print(df.head())

    print("\nColonnes :")
    print(df.columns)

    print("\nValeurs manquantes :")
    print(df.isna().sum())

    print("\nStatistiques :")
    print(df.describe())

if __name__ == "__main__":
    validate_data()

