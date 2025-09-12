import pandas as pd
import numpy as np

#caminho do arquivo no desk
file_path = r"C:\Users\jessy\Documents\portfolio-ecommerce\data\raw\data.csv"

#carregar o dataset
df = pd.read_csv(file_path, encoding="latin1")

#mostrar o caminho do dataset
print("Formato do dataset (linhas, colunas: )", df.shape)

#mostrar as 5 primeiras linhas
#print(df.head(10))

#verificação de valores nulos
#print(df.isnull().sum())

#conferir os tipos de dados
print(df.info())