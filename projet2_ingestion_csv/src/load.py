""" Script: charge le fichier sales_clean, crée le fichier final, ajoute une petite info (= unité vendue : moyenne par employé)"""

import pandas as pd

def load_final_data():
    df = pd.read_csv("../data/processed/sales_clean.csv")

    # Ajouter une statistique
    df["avg_units_sold_global"] = df["Units Sold"].mean()

    df.to_csv("../data/final/final_sales.csv", index=False)
    print("Chargement terminé, fichier final créé !")

if __name__ == "__main__":
    load_final_data()
