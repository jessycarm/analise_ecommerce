#--------- Passo 0: Importar e Carregar ---------------
# importação das bibliotecas
import pandas as pd
import numpy as np

# carregar o arquivo
file_path = r"C:\Users\jessy\Documents\portfolio-ecommerce\data\raw\data.csv"
df = pd.read_csv( file_path, encoding="latin1")

# -------- Passo 1: Entendimento Inicial: Checando as estruturas -----------------

print(df.shape) #verificar linhas e colunas
print(df.head()) #amostra de dados
print(df.info()) #tipos de valores, not-null counts
print(df.isnull().sum()) #verificar os valores nulos

# --------- Passo 2: Correção dos tipos de dados ------------------------
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce') #ajuste do formato da data
df['CustomerID'] = df['CustomerID'].astype('Int64') #transformação no tipo inteiro
df['InvoiceNo'] = df['InvoiceNo'].astype(str) #transformação no tipo string
df['StockCode'] = df['StockCode'].astype(str) #transformação no tipo string
df['Country'] = df['Country'].astype('category') #transformação em campo categórico para otimiizar memória

print(f"\nDados após correção: \n{df.info()}") #verificação


# --------- Passo 3: Tratar os valores que estão ausentes ------------------------
#verificar a proporção de nulos em CustomerID
n_total = len(df)
n_missing_cust = df['CustomerID'].isna().sum()
print(f"\nCustomerID missing: {n_missing_cust} ({n_missing_cust/n_total:.1%})")

#criar coluna auxiliar para identificar os clientes conhecidos e não conhecidos
df['customer_known'] = df['CustomerID'].notna()
# criando um dataframe só com os clientes conhecidos
df_customers = df[df['customer_known']].copy()

print(f"Dados após tratamento do CustomerID: \n{df.head()}") #conferencia de implantação

#tratamento do Description
df['Description'] = df['Description'].fillna('missing_description')

description_unicas = df['Description'].unique() #função para retornar valores unicos de descrições
print(f"Dados após tratamento do Description: \n{df['Description'].head()}, \n{description_unicas}") #conferencia de implantação


# --------- Passo 4: Tratar as duplicatas ---------------------
print(f"\nQuantidade de duplicatas: {df.duplicated().sum()}") #checagem de duplicatas

#calculando a porcentagem
v_total = len(df)
v_dupl = df.duplicated().sum()
print(f"\nPorcentagem de Duplicatas: ({v_dupl/v_total:.3%})")

#apagando as duplicatas exatas
df = df.drop_duplicates()
print(f"\nQuantidade de duplicatas após limpeza: {df.duplicated().sum()}")#checagem

#busca de duplicatas parciais
duplicatas_parciais = df.duplicated(subset = ['InvoiceNo', 'StockCode'])
print(f"\nQuantidade de duplicatas parciais em InvoiceNo + StockCode: {duplicatas_parciais.sum()}")

#verificação das duplicatas
df_duplicatas_parciais = df[df.duplicated(subset = ['InvoiceNo', 'StockCode'], keep = False)]
print(f"\nEsses são os dados duplicados:\n{df_duplicatas_parciais}")

# --------- Passo 5: Detectar e tratar as devoluções e cancelamentos ---------------------

#marcar a devolução
df['is_return'] = df['Quantity'] < 0
#quantidade de registros de devolução
df['is_return'].sum(), (df['is_return'].mean()*1000).round(2)

num_devolucoes = df['is_return'].sum()
taxa_por_mil = ((df['is_return'].mean()*1000).round(2))

print("\nQuantidade de devoluções:", num_devolucoes)
print(f"Taxa por mil registros: {taxa_por_mil}%")