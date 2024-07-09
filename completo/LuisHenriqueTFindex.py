#Aluno: Luis Henrique de Melo Santiago
#Turma: BSI23

import pandas as pd
from funcoes import relat_arrecadacao, cria_arq_dados_uf, dados_imp_e_exp, estat_imp_e_exp, estat_ipi_beb_e_fumo, pesq_ano_mes_uf


pd.set_option('display.float_format', lambda x: '%.2f' % x)

#------------------------------------------------------

def convert_num(val):
    if ',' in val[-3:] or '.' in val[-3:]:  # (verificar centavos) ante-penultimo caracter for . ou ,
        val = val[:-3].replace(',', '').replace('.', '') + val[-3:].replace(',', '.')
    else:
        val = val.replace(',', '').replace('.', '')

    return val

#------------------------------------------------------

def entrada_mensagem(tam=80):

    out = [
        "- Relatório do Documento arrecadação",
        "- Criar arquivo com dados de um UF específico",
        "- Dados de Importação e exportação",
        "- Estatística dos dados de Importação e Exportação",
        "- Estatística dos dados de IPI de fumo e bebidas",
        "- Verificar a existencia de um dado nas colunas Ano, Mês, UF"
    ]

    out = [f"{out[i]} = Tecla {i+1}" for i in range(len(out))]
    out.append("Sair = 0")



    print('=' * tam)
    print("||" + "Bem vindo ao software de Análise da Arrecadação por Estado anos 2000 e 2023.".center(tam - 4) + "||")
    print("||" + " ".center(tam - 4) + "||")

    for line in out:
        print(f"|| {line.ljust(tam - 6)} ||")

    print('=' * tam)


#------------------------------------------------------

def escolher_opcao():
    try:
        n = int(input("Por favor, insira um número válido, até 6: "))
        return n
    except ValueError:
        print("Por favor, insira um número válido.")
        return escolher_opcao()


def main():

    df = pd.read_csv('arrecadacao-estado.csv', sep=';', encoding='latin-1')
    df['Ano'] = df['Ano'].astype(int) 
    df['IMPOSTO SOBRE IMPORTAÇÃO'] = df['IMPOSTO SOBRE IMPORTAÇÃO'].apply(convert_num).astype(float)
    df['IMPOSTO SOBRE EXPORTAÇÃO'] = df['IMPOSTO SOBRE EXPORTAÇÃO'].apply(convert_num).astype(float)
    df['IPI - FUMO'] = df['IPI - FUMO'].apply(convert_num).astype(float)
    df['IPI - BEBIDAS'] = df['IPI - BEBIDAS'].apply(convert_num).astype(float)

    while True:
        entrada_mensagem()
        n = escolher_opcao()
        
        if n == 1:
            print("\n========== Executando ==========")
            print("\n========== Relatório de linhas e colunas do Documento ==========")
            relat_arrecadacao(df)
            

        elif n == 2:
            print("\n========== Executando ==========")
            estado = input("Entre com o estado (deve estar em UF - 2 letras) a ser filtrado: ")
            nome_arquivo = input("Entre com o nome do arquivo (não colocar extensão no final): ")
            usar_relat_arrecadacao = bool(int(input("Entre se deseja ver o relatório de linhas e colunas do documento, relatório (use 0 (não) ou 1 (sim)): ")))
            
            if usar_relat_arrecadacao:
                print("\n========== Executando ==========")
                print("\n========== Relatório de linhas e colunas do Documento ==========")

            cria_arq_dados_uf(df, nome_arquivo, estado, usar_relat_arrecadacao)
            print(f"\n========== Arquivo com dados do estado {estado} criado com sucesso! ==========")

        elif n == 3:
            print("\n========== Executando ==========")
            print("\nDados soma dos dados de importação e exportação agrupados por ano de 2000 a 2023:")
            dados_imp_e_exp(df)

        elif n == 4:
            print("\n========== Executando ==========")
            print("\n Estatística dos dados de importação e exportação do ano 2000 a 2023:")

            estat_imp_e_exp(df)

        elif n == 5:
            print("\n========== Executando ==========")
            print("\n Estatística dos dados de IPI - FUMO e IPI - BEBIDAS do ano 2000 a 2023:")

            estat_ipi_beb_e_fumo(df)
            
        elif n == 6:
            print("\n========== Executando ==========")   
            val = input("Insira um valor para filtrar nas colunas Ano, Mês (por extenso), UF(Duas Letras): ")
            print(f"\n Abaixo temos a relação de presença ou ausência do dado {val} no documento:")
            pesq_ano_mes_uf(df, val)
            
        elif n == 0:
            print('\nObrigado por usar o programa.')
            break
            
        else:
            print("Não compreendi.")
            n = int(input("Por favor, insira um número válido, até 6: "))  


if __name__ == '__main__':
    main()