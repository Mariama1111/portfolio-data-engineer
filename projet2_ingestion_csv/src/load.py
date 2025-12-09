""" Script: charge le fichier sales_clean, crée le fichier final, ajoute une petite info (= unité vendue moyenne par employé)"""

import pandas as pd

def load_final_data():
    df = pd.read_csv("../data/processed/sales_clean.csv")

    # Exemple de chargement : ajouter une statistique
    avg_units = df["Units Sold"].mean()
    df["avg_units_sold_global"] = avg_units

    df.to_csv("../data/final/final_sales.csv", index=False)
    print("Chargement terminé, fichier final créé !")

if __name__ == "__main__":
    load_final_data()
