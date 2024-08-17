[**English**]

# Interactive Visualization of ENEM 2023

This project aims to create an interactive visualization of the ENEM 2023 data using Python and Tableau Public.

## Project Description

I used the Pandas library in Python to perform the following steps:

- **Data Analysis:** Counting the number of registered candidates and calculating the participation percentage in each Brazilian municipality that administered the ENEM exam in 2023.
- **Integration with Geospatial Data:** The data was concatenated with a geospatial reference table (latitude and longitude) for each Brazilian municipality.
- The processed data was, then, uploaded to Tableau Public to create interactive visualizations.

## Interactive Visualizations

The interactive visualizations of the project can be accessed through the following links:  

Total of Registered Candidates and Attendance (%) by Municipality  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporMunicpio/MapGeral  

Total of Registered Candidates and Attendance (%) by Time Zone  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporFusoHorrio/MapFusoHorrio  

## How to Use

Clone this repository.  
Download the ENEM 2023 data at https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.  
Run the Python script to generate the necessary data.  
The generated data (geo_plus_education_data.csv) can be visualized using Tableau Public.

## Requirements

- Python 3.x  
- Pandas  
- Tableau Public

---