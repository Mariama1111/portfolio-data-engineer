""" Import librairie, définition de fonction de téléchargement du fichier public sales.csv et enregistrement dans dossier /data/raw..."""

import pandas as pd

def load_sales_data():
    url = "https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv"
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    df = load_sales_data()
    df.to_csv("../data/raw/sales.csv", index=False)
    print("CSV de ventes téléchargé et sauvegardé !")
