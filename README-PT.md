[**Português**]

# Visualização Interativa do ENEM 2023

Este projeto tem como objetivo criar uma visualização interativa dos dados do ENEM 2023, utilizando Python e Tableau Public.

## Descrição do Projeto

Utilizei a biblioteca Pandas no Python para realizar as seguintes etapas:

- **Análise de Dados:** Contagem da quantidade de inscritos e cálculo da porcentagem de participação em cada município do Brasil que aplicou a prova do ENEM em 2023.
- **Integração com Dados Geoespaciais:** Os dados foram concatenados com uma tabela de referência geoespacial (latitude e longitude) de cada município do Brasil.
- Os dados processados foram, então, inseridos no Tableau Public para a criação de visualizações interativas.

## Visualizações Interativas

As visualizações interativas do projeto podem ser acessadas nos seguintes links:  

Total de Inscritos e Presença (%) por Município  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporMunicpio/MapGeral  

Total de Inscritos e Presença (%) por Fuso Horário  
https://public.tableau.com/app/profile/jeanferrer/viz/ENEM2023-TotaldeInscritosePresenaporFusoHorrio/MapFusoHorrio  

## Como Utilizar

Clone este repositório.  
Baixe os dados do ENEM 2023 em https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.  
Execute o script Python para gerar os dados necessários.  
Os dados gerados (geo_plus_education_data.csv) podem ser visualizados utilizando o Tableau Public.

## Requisitos

- Python 3.x  
- Pandas  
- Tableau Public

---