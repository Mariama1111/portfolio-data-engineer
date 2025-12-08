""" import de la librairie pandas, téléchargement du dataset public BostonHousing et enregistrement dans le dossier /data/raw..."""

import pandas as pd

def load_raw_data():
  url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
  df = pd.read_csv(url)
  return df

if __name__ == "__main__":
    df = load_raw_data()
    df.to_csv("../data/raw/housing.csv", index=False)
    print("Données brutes téléchargées et sauvegardées !")
