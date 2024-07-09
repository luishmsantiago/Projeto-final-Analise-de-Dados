import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)

#------------------------------------------------------
def convert_num(val):
    if ',' in val[-3:] or '.' in val[-3:]:  # (verificar centavos) ante-penultimo caracter for . ou ,
        val = val[:-3].replace(',', '').replace('.', '') + val[-3:].replace(',', '.')
    else:
        val = val.replace(',', '').replace('.', '')

    return val
#------------------------------------------------------
start = print("Bem vindo ao software de análise dos dados da Arrecadação por Estado entre os anos 2000 e 2023.")
Funcoes = print("""Função 1 = Tecla 1; \nFunção 2 = Tecla 2; \nFunção 3 = Tecla 3; \nFunção 4 = Tecla 4; \nFunção 5 = Tecla 5; \nFunção 6 = Tecla 6; \nSair = 0.""" )
n = int(input("Por favor, insira um valor válido, até 6: "))

df = pd.read_csv('arrecadacao-estado.csv', sep=';', encoding='latin-1')
df['Ano'] = df['Ano'].astype(int) 
df['IMPOSTO SOBRE IMPORTAÇÃO'] = df['IMPOSTO SOBRE IMPORTAÇÃO'].apply(convert_num).astype(float)
df['IMPOSTO SOBRE EXPORTAÇÃO'] = df['IMPOSTO SOBRE EXPORTAÇÃO'].apply(convert_num).astype(float)
# df = df.dropna(subset=['IPI - FUMO', 'IPI - BEBIDAS'])

# df['IPI - FUMO'] = df['IPI - FUMO'].apply(convert_num).astype(float)
# df['IPI - BEBIDAS'] = df['IPI - BEBIDAS'].apply(convert_num).astype(float)

#------------------------------------------------------
def funcao1(df):
    linhas, colunas = df.shape
    nome_colunas = df.columns.tolist()
    print(f"Linhas: {linhas}")
    print(f"Linhas: {colunas}")
    out = '\n  - '.join(nome_colunas)
    print(f"Nome Colunas:\n  - {out}")

funcao1(df)
#------------------------------------------------------
def funcao2(df, nome_arquivo, estado_filtro, usar_funcao1=False):
    
    if usar_funcao1:
        funcao1(df)

    new_df = df.query(f"UF == '{estado_filtro}'")
    new_df.to_csv(f"{nome_arquivo}.csv", index=False)

arquivo_salvar = 'my_MG'
df2 = funcao2(df, arquivo_salvar, 'MG', usar_funcao1=True)

#------------------------------------------------------
def funcao3(df):
    print(df[['Ano', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].groupby('Ano', as_index=False).sum())

funcao3(df)
#------------------------------------------------------
def funcao4(df):
    media_impor, media_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].mean()
    desvio_impor, desvio_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].std()
    mediana_impor, mediana_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].median()
    print(f"Media Imp. Importação: {media_impor:.2f} \tMedia Imp. Exportação: {media_expor:.2f}")
    print(f"Media Imp. Importação: {desvio_impor:.2f} \tMedia Imp. Exportação: {desvio_expor:.2f}")
    print(f"Media Imp. Importação: {mediana_impor:.2f} \tMedia Imp. Exportação: {mediana_expor:.2f}")

funcao4(df)
#------------------------------------------------------
def funcao5(df):
    pass
    # media_fumo, media_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].mean()
    # desvio_fumo, desvio_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].std()
    # mediana_fumo, mediana_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].median()
    # print(f"Media IPI - FUMO: {media_fumo:.2f} \tMedia IPI - BEBIDAS: {media_bebidas:.2f}")
    # print(f"Media IPI - FUMO: {desvio_fumo:.2f} \tMedia IPI - BEBIDAS: {desvio_bebidas:.2f}")
    # print(f"Media IPI - FUMO: {mediana_fumo:.2f} \tMedia IPI - BEBIDAS: {mediana_bebidas:.2f}")

#funcao5(df)
#------------------------------------------------------
def funcao6(df):
    pass
    # print(int(input("""Insira o que tem interesse em saber:\n
    #             1) IPI - VINCULADO À IMPORTACAO\n
    #             2) IPI - OUTROS
    #             3) IPI - AUTOMÓVEIS
    #             4) RECEITA PREVIDENCIÁRIA
    #             5) ADMINISTRADAS POR OUTROS ÓRGÃOS""")))
    # print(int(input("Insira o ano de interesse entre 2000 e 2023")))
    
    # media_impor, media_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].mean()
    # desvio_impor, desvio_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].std()
    # mediana_impor, mediana_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].median()
    # print(f"Media Imp. Importação: {media_impor:.2f} \tMedia Imp. Exportação: {media_expor:.2f}")
    # print(f"Media Imp. Importação: {desvio_impor:.2f} \tMedia Imp. Exportação: {desvio_expor:.2f}")
    # print(f"Media Imp. Importação: {mediana_impor:.2f} \tMedia Imp. Exportação: {mediana_expor:.2f}")



#------------------------------------------------------

def main(n):
    df = pd.read_csv('arrecadacao-estado.csv', sep=';', encoding='latin-1')
    df['Ano'] = df['Ano'].astype(int) 
    df['IMPOSTO SOBRE IMPORTAÇÃO'] = df['IMPOSTO SOBRE IMPORTAÇÃO'].apply(convert_num).astype(float)
    df['IMPOSTO SOBRE EXPORTAÇÃO'] = df['IMPOSTO SOBRE EXPORTAÇÃO'].apply(convert_num).astype(float)
    

    while True:

        if n == 1:

            print("========== Executando Função 1 ==========")
            funcao1(df)

        elif n == 2:

            print("\n========== Executando Função 2 ==========")
            estado = input("Entre com o estado a ser filtrado: ")
            nome_arquivo = input("Entre com o nome do arquivo: ")
            usar_funcao1 = bool(int(input("Entre se deseja usar a funcao1 (use 0 ou 1): ")))
            if usar_funcao1:
                print("=========> Funcao1 será executada")

            funcao2(df, nome_arquivo, estado, usar_funcao1)

        elif n == 3:

            print("\n========== Executando Função 3 ==========")
            print("Dados soma dos dados de importação e exportação agrupados por ano")
            funcao3(df)

        elif n == 4:

            print("\n========== Executando Função 4 ==========")
            funcao4(df)

        elif n == 5:

            print("\n========== Executando Função 5 ==========")
            funcao5(df)
        
        elif n == 6: 

            print("\n========== Executando Função 6 ==========")
            #funcao6(df)
        
        elif n == 0:
            print('Obrigado por usar o programa.')
            break
        
        else:
            print("Não compreendi.")
            n = int(input("Por favor, insira um valor válido, até 6: "))

if __name__ == '__main__':
    main(n)
