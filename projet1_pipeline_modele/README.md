### 🧠 Projet 1 – Pipeline ETL + Modèle de Machine Learning

Ce projet démontre ma capacité à construire un pipeline complet :
- Extraction des données
- Transformation & nettoyage
- Split train/test
- Entraînement d’un modèle
- Évaluation (MSE, R²)
- Prédiction
- Export final

Le dataset utilisé est : Boston Housing.

#### 📂 Structure
```bash
projet1_pipeline_modele/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│ 
├── models/
│   └── model.pkl
│
└── src/
    ├── extract.py
    ├── transform.py
    ├── train_model.py
    ├── validate.py
    ├── predict.py
    └── load.py
```
________________________________
#### ⚙️ Pipeline
1️⃣ Extract

Télécharge le dataset Boston Housing et le stocke dans data/raw/.

```bash
python extract.py
```

2️⃣ Transform

- Nettoyage
- Suppression des NA
- Conversion numérique
- Renommage de la target
```bash
python transform.py
```

3️⃣ Train
- Linear Regression
- Sauvegarde du modèle model.pkl
```bash
python train_model.py
```

4️⃣ Validate
- R²
- MSE
```bash
python validate.py
```

5️⃣ Predict

Génère une prédiction sur un exemple.
```bash
python predict.py
```

6️⃣ Load

Exporte un fichier final contenant les prédictions.
```bash
python load.py
```
___________________________________
#### 📊 Performance (exemple)
- R² : ~0.70 – 0.75
- MSE : ~22
Ce sont des valeurs attendues pour ce dataset.
___________________________________
#### 🧹 Améliorations possibles

- Ajouter une pipeline Scikit-Learn complète
- Intégrer MLflow pour le suivi du modèle
- Automatiser via Airflow ou Prefect
