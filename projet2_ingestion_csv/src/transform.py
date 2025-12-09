"""Script : nettoie les valeurs manquantes ; renomme les colonnes ; sauvegarde les données propres"""

import pandas as pd

def clean_sales_data():
    # Charger le fichier extrait
    df = pd.read_csv("../data/raw/sales.csv")

    # Renommer les colonnes pour être cohérent
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Supprimer les lignes vides
    df = df.dropna()

    # Sauvegarder
    df.to_csv("../data/processed/sales_clean.csv", index=False)
    print("Données transformées et sauvegardées !")

if __name__ == "__main__":
    clean_sales_data()
