#Converte o arquivo para matriz 

import indice
import pandas as pd

def funcao_um(df):
    linhas, colunas = df.shape
    nome_colunas = df.columns.tolist()
    print(f"Linhas: {linhas}")
    print(f"Linhas: {colunas}")
    out = '\n  - '.join(nome_colunas)
    print(f"Nome Colunas:\n  - {out}")

def convert_num(val):
    if ',' in val[-3:] or '.' in val[-3:]:  # (verificar centavos) ante-penultimo caracter for . ou ,
        val = val[:-3].replace(',', '').replace('.', '') + val[-3:].replace(',', '.')
    else:
        val = val.replace(',', '').replace('.', '')

    return val

df = pd.read_csv('arrecadacao-estado.csv', sep=';', encoding='latin-1')
df['Ano'] = df['Ano'].astype(int) 
df['IMPOSTO SOBRE IMPORTAÇÃO'] = df['IMPOSTO SOBRE IMPORTAÇÃO'].apply(convert_num).astype(float)
df['IMPOSTO SOBRE EXPORTAÇÃO'] = df['IMPOSTO SOBRE EXPORTAÇÃO'].apply(convert_num).astype(float)


funcao_um(df)



