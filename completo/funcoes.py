#Aluno: Luis Henrique de Melo Santiago
#Turma: BSI23

#------------------------------------------------------
def relat_arrecadacao(df):
    linhas, colunas = df.shape #torna tupla de linhas e colunas
    nome_colunas = df.columns.tolist()
    print(f"Linhas: {linhas}")
    print(f"Colunas: {colunas}")
    out = '\n  - '.join(nome_colunas)
    print(f"Nome Colunas:\n  - {out}")

#------------------------------------------------------
def cria_arq_dados_uf(df, nome_arquivo, estado_filtro, usar_relat_arrecadacao=False):
    
    if usar_relat_arrecadacao:
        relat_arrecadacao(df)

    new_df = df[df['UF'].str.contains(estado_filtro, case=False)]
    new_df.to_csv(f"{nome_arquivo}.csv", index=False)

#------------------------------------------------------
def dados_imp_e_exp(df):
    colunas = ['Ano', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']
    print(df[colunas].groupby('Ano', as_index=False).sum())

#------------------------------------------------------
def estat_imp_e_exp(df):
    media_impor, media_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].mean()
    desvio_impor, desvio_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].std()
    mediana_impor, mediana_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].median()
    print(f"Media Imp. Importação: {media_impor:.2f} \tMedia Imp. Exportação: {media_expor:.2f}")
    print(f"Desvio Padrão Imp. Import.: {desvio_impor:.2f}   Desvio Padrão Imp. Export.: {desvio_expor:.2f}")
    print(f"Mediana Imp. Importação: {mediana_impor:.2f} \tMediana Imp. Exportação: {mediana_expor:.2f}")

#------------------------------------------------------
def estat_ipi_beb_e_fumo(df):
    media_fumo, media_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].mean()
    desvio_fumo, desvio_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].std()
    mediana_fumo, mediana_bebidas = df[['IPI - FUMO', 'IPI - BEBIDAS']].median()
    print(f"Media IPI - FUMO: {media_fumo:.2f} \tMedia IPI - BEBIDAS: {media_bebidas:.2f}")
    print(f"Desvio Pad. IPI - FUMO: {desvio_fumo:.2f} \tDesvio Pad. IPI - BEBIDAS: {desvio_bebidas:.2f}")
    print(f"Mediana IPI - FUMO: {mediana_fumo:.2f} \tMediana IPI - BEBIDAS: {mediana_bebidas:.2f}")

#------------------------------------------------------
def pesq_ano_mes_uf(df, val):
    cols = ['Ano', 'Mês', 'UF']
    df = df[cols]

    for col in cols:
        serie = df[col].astype(str)
        df_result = df[serie.str.contains(val, case=False)]
                    
        if len(df_result) > 0:
            print(df_result)
            return
    
    print("Nenhum valor encontrado!")