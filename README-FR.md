[**Français**]

# Visualisation Interactive du ENEM 2023

Ce projet vise à créer une visualisation interactive des données ENEM 2023 à l'aide de Python et Tableau Public.

## Description du Projet

J'ai utilisé la bibliothèque Pandas en Python pour réaliser les étapes suivantes:

- **Analyse de Données :** Comptage du nombre d'inscrits et calcul du pourcentage de participation dans chaque municipalité du Brésil qui a administré l'examen du ENEM en 2023.
- **Intégration avec des Données Géospatiales :** Les données ont été concaténées avec un tableau de référence géospatiale (latitude et longitude) de chaque municipalité du Brésil.
- Les données traitées ont ensuite été insérées dans Tableau Public pour la création de visualisations interactives.

## Visualisations Interactives

Les visualisations interactives du projet peuvent être consultées aux liens suivants:  

Total de Candidats Inscrits et Taux de Participation (%) par Municipalité  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporMunicpio/MapGeral  

Total de Candidats Inscrits et Taux de Participation (%) par Fuseau Horaire  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporFusoHorrio/MapFusoHorrio  

## Comment Utiliser

Clonez ce dépôt.  
Téléchargez les données du ENEM 2023 sur https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.  
Exécutez le script Python pour générer les données nécessaires.  
Les données générées (geo_plus_education_data.csv) peuvent être visualisées en utilisant Tableau Public.

## Exigences

- Python 3.x  
- Pandas  
- Tableau Public

---