import indice as id

def funcao4(df):
    media_impor, media_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].mean()
    desvio_impor, desvio_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].std()
    mediana_impor, mediana_expor = df[['IMPOSTO SOBRE IMPORTAÇÃO', 'IMPOSTO SOBRE EXPORTAÇÃO']].median()
    print(f"Media Imp. Importação: {media_impor:.2f} \tMedia Imp. Exportação: {media_expor:.2f}")
    print(f"Media Imp. Importação: {desvio_impor:.2f} \tMedia Imp. Exportação: {desvio_expor:.2f}")
    print(f"Media Imp. Importação: {mediana_impor:.2f} \tMedia Imp. Exportação: {mediana_expor:.2f}")

funcao4(id.df)