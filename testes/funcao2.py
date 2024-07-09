import pandas as pd
import indice
import funcao1 as fc1
# start = print("Bem vindo ao software de análise dos dados da Arrecadação por Estado entre os anos 2000 e 2023.")
# Funcoes = print("""Função 1 = Tecla 1; \nFunção 2 = Tecla 2; \nFunção 3 = Tecla 3; \nFunção 4 = Tecla 4; \nFunção 5 = Tecla 5; \nFunção 6 = Tecla 6; \nSair = 0.""" )
# n = int(input("Por favor, insira um valor válido, até 6: "))

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

def funcao2(df, nome_arquivo, estado_filtro, usar_funcao1=False):
    
    if usar_funcao1:
        fc1.funcao1(df)

    new_df = df.query(f"UF == '{estado_filtro}'")
    new_df.to_csv(f"{nome_arquivo}.csv", index=False)

arquivo_salvar = 'my_MG'
df2 = funcao2(df, arquivo_salvar, 'MG', usar_funcao1=True)
