# Bibliotecas utilizadas
import pandas as pd


# Carregando os dados do ENEM
enem_data = pd.read_csv('MICRODADOS_ENEM_2023.csv', encoding='latin-1', sep=';')
# Mostrando o header
enem_data.head()


# Contagem de participantes por cidade (código do IBGE da cidade: participantes)
value_counts_per_city_total = enem_data.CO_MUNICIPIO_PROVA.value_counts()
print(value_counts_per_city_total)

# Filtrando os dados do enem para somente os que tiveram presença em todas as provas
enem_data_present = enem_data[
    (enem_data.TP_PRESENCA_CN == 1) & 
    (enem_data.TP_PRESENCA_CH == 1) & 
    (enem_data.TP_PRESENCA_LC == 1) &
    (enem_data.TP_PRESENCA_MT == 1)]

# Contagem de participantes presentes por cidade (código do IBGE da cidade: participantes)
value_counts_per_city_present = enem_data_present.CO_MUNICIPIO_PROVA.value_counts()
print(value_counts_per_city_present)


# Alinhando as pandas.Series por código de cidade do IBGE
aligned_present_total = value_counts_per_city_present.align(value_counts_per_city_total, join='right', fill_value=0)
# Proporção de participantes presentes por cidade (código do IBGE da cidade: porcentagem de participantes)
percentage_present_per_city = (aligned_present_total[0] / aligned_present_total[1]) * 100
print(round(percentage_present_per_city, 2))

# Carregando os dados geoespaciais dos municípios do Brasil
geo_data = pd.read_csv('municipios.csv')
# Mostrando o header
geo_data.head()


# Convertendo value_counts_per_city_total de um pandas.Series para um pandas.DataFrame
value_counts_per_city_total = value_counts_per_city_total.reset_index()
value_counts_per_city_total.columns = ['codigo_ibge', 'total_applicants']

# Convertendo percentage_present_per_city de um pandas.Series para um pandas.DataFrame
percentage_present_per_city = percentage_present_per_city.reset_index()
percentage_present_per_city.columns = ['codigo_ibge', 'percentage_present']

# Colocando CO_MUNICIPIO_PROVA:codigo_ibge como referência para a união dos dataframes
value_counts_per_city_total = value_counts_per_city_total.rename(columns={'CO_MUNICIPIO_PROVA': 'codigo_ibge'})
percentage_present_per_city = percentage_present_per_city.rename(columns={'CO_MUNICIPIO_PROVA': 'codigo_ibge'})

# Mesclando o dataframe de dados geoespaciais com a respectiva porcentagem de participação no ENEM
geo_plus_education_data = pd.merge(geo_data, value_counts_per_city_total, on='codigo_ibge', how='left', suffixes=('', '_education'))
geo_plus_education_data = pd.merge(geo_plus_education_data, percentage_present_per_city, on='codigo_ibge', how='left', suffixes=('', '_percentage'))
print(geo_plus_education_data.head())


# Exportando o dataframe para um arquivo .csv
geo_plus_education_data.to_csv('geo_plus_education_data.csv', index=False)