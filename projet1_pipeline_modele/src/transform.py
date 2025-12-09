""" Script de suppression de lignes vides, renomme la colonne cible, sauvegarde des données transfomées"""

import pandas as pd

def transform_data(input_path="../data/raw/housing.csv",
                   output_path="../data/processed/housing_clean.csv"):
    df = pd.read_csv(input_path)
    
    # Supprimer les lignes avec NaN
    df = df.dropna()
    
    # Renommer la colonne cible
    df = df.rename(columns={'medv': 'target'})
    
    # Convertir toutes les colonnes en float
    for col in df.columns:
        df[col] = df[col].astype(float)
    
    df.to_csv(output_path, index=False)
    print(f"Données transformées sauvegardées : {output_path}")
    return df

if __name__ == "__main__":
    transform_data()
