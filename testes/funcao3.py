import indice as id


def funcao3(df):
    print(df[['Ano', 'IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].groupby('Ano', as_index=False).sum())

funcao3(id.df)