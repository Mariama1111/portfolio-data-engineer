# portfolio-data-engineer
Data Engineer - Alternance 

# Projet 1 – Pipeline de données + Modèle simple

## Objectif
Construire un pipeline complet : extraction → nettoyage → stockage → modèle → prédictions.

## Pipeline
1. Extraction des données (dataset Housing Prices)
2. Transformations (nettoyage)
3. Chargement dans SQLite
4. Entraînement d’un modèle (régression linéaire)
5. Génération d’un fichier de prédictions

## Structure
- `src/` : scripts Python
- `data/` : données brutes et transformées
- `output/` : résultats (prédictions)
- `diagrams/` : schémas du pipeline

## Technologies
Python, Pandas, Scikit-learn, SQLite.
_____________________________________________________________________________________________________

# Projet 2 – Pipeline d’ingestion de fichiers CSV

## Objectif
Créer un pipeline simple : ingestion → validation → transformation → chargement en base.

## Pipeline
1. Récupération de fichiers CSV (données de ventes)
2. Vérification du schéma
3. Nettoyage / corrections de types
4. Chargement dans une base SQLite

## Structure
- `src/` : scripts Python (extract, validate, transform, load)
- `data/` : raw + cleaned
- `diagrams/` : schéma du pipeline

## Technologies
Python, Pandas, SQLite.
