"""Script : supprime lignes vides ; transforme les dates ;  corrige les colonnes numériques ; sauvegarde les données propres"""

import pandas as pd

def transform_sales(df):
    # Supprimer les lignes avec valeurs manquantes
    df = df.dropna()
    
    # Convertir la colonne 'date' en format datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Corriger les types numériques
    numeric_cols = ['total', 'quantity']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/sales.csv")
    df_clean = transform_sales(df)
    df_clean.to_csv("../data/cleaned/sales_clean.csv", index=False)
    print("CSV transformé et sauvegardé !")
