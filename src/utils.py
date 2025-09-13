import pandas as pd

def padronizar_description(df):
    df['Description'] = df['Description'].astype(str).str.strip().str.upper()
    return df

def padronizar_country(df, mapa_paises):
    df['Country'] = df['Country'].astype(str).str.strip().str.upper()
    df['Country'] = df['Country'].replace(mapa_paises)
    return df
