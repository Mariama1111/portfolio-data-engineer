#### 🧠Projet 2 – Ingestion & Validation CSV

Ce projet montre comment construire un pipeline d’ingestion simple mais robuste :
- Extraction d’un CSV en ligne
- Vérification de l’intégrité
- Nettoyage
- Validation statistique
- Export final

Dataset utilisé : sales_success.csv de Plotly.
__________________________________
#### 📂 Structure
``` bash
projet2_ingestion_csv/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
└── src/
    ├── extract.py
    ├── transform.py
    ├── validate.py
    └── load.py
```
___________________________________
#### ⚙️ Pipeline

1️⃣ Extract

Télécharge le fichier CSV depuis internet.
```bash
python extract.py
```

2️⃣ Transform
- Nettoyage basique
- Normalisation des noms de colonnes
- Vérification des types
```bash
python transform.py
```

3️⃣ Validate

Affiche :
- aperçu des données
- statistiques
- vérification NA et incohérences
```bash
python validate.py
```

4️⃣ Load

Génère un fichier analytique final.
```bash
python load.py
```
_______________________________
***Fichiers générés :***

data/raw/sales.csv

data/processed/sales_clean.csv

data/final/final_sales.csv
_______________________________
#### 🧹 Améliorations possibles

- Ajout de règles métier (seuils, anomalies)
- Intégration d’un data quality checker (Great Expectations)
- Stockage dans un data lake (S3, ADLS)
