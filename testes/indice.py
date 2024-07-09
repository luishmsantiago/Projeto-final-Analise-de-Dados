import pandas as pd
import funcao1 as fc1
import funcao2 as fc2
import funcao3 as fc3
import funcao4 as fc4
import funcao5 as fc5
import funcao6 as fc6

pd.set_option('display.float_format', lambda x: '%.2f' % x)

#------------------------------------------------------

def convert_num(val):
    if ',' in val[-3:] or '.' in val[-3:]:  # (verificar centavos) ante-penultimo caracter for . ou ,
        val = val[:-3].replace(',', '').replace('.', '') + val[-3:].replace(',', '.')
    else:
        val = val.replace(',', '').replace('.', '')

    return val

#------------------------------------------------------

def entrada_mensagem():
    print("Bem vindo ao software de análise dos dados da Arrecadação por Estado entre os anos 2000 e 2023.")
    print("""Função 1 = Tecla 1; \nFunção 2 = Tecla 2; \nFunção 3 = Tecla 3; \nFunção 4 = Tecla 4; \nFunção 5 = Tecla 5; \nFunção 6 = Tecla 6; \nSair = 0.""" )
    
#------------------------------------------------------

def escolher_opcao():
    try:
        n = int(input("Por favor, insira um valor válido, até 6: "))
        return n
    except ValueError:
        print("Por favor, insira um número válido.")
        return escolher_opcao()


def main():

    df = pd.read_csv('arrecadacao-estado.csv', sep=';', encoding='latin-1')
    df['Ano'] = df['Ano'].astype(int) 
    df['IMPOSTO SOBRE IMPORTAÇÃO'] = df['IMPOSTO SOBRE IMPORTAÇÃO'].apply(convert_num).astype(float)
    df['IMPOSTO SOBRE EXPORTAÇÃO'] = df['IMPOSTO SOBRE EXPORTAÇÃO'].apply(convert_num).astype(float)
    
    # df = df.dropna(subset=['IPI - FUMO', 'IPI - BEBIDAS'])
    # df['IPI - FUMO'] = df['IPI - FUMO'].apply(convert_num).astype(float)
    # df['IPI - BEBIDAS'] = df['IPI - BEBIDAS'].apply(convert_num).astype(float)


    while True:
        entrada_mensagem()
        escolher_opcao()

        if n == 1:

            print("========== Executando Função 1 ==========")
            fc1.funcao_um(df)
            

        elif n == 2:
            print("\n========== Executando Função 2 ==========")
            estado = input("Entre com o estado a ser filtrado: ")
            nome_arquivo = input("Entre com o nome do arquivo: ")
            usar_funcao1 = bool(int(input("Entre se deseja usar a funcao1 (use 0 ou 1): ")))
            
            if usar_funcao1:
                print("=========> Funcao1 será executada")

            fc2.funcao2(df, nome_arquivo, estado, usar_funcao1)

        elif n == 3:
            print("\n========== Executando Função 3 ==========")
            print("Dados soma dos dados de importação e exportação agrupados por ano")
            fc3.funcao3(df)

        elif n == 4:
            print("\n========== Executando Função 4 ==========")
            fc4.funcao4(df)

        elif n == 5:
            print("\n========== Executando Função 5 ==========")
            fc5.funcao5(df)
            
        elif n == 6:   
            print("\n========== Executando Função 6 ==========")
            pass
            # fc6.funcao6(df)
            
        elif n == 0:
            print('Obrigado por usar o programa.')
            
        else:
            print("Não compreendi.")
            n = int(input("Por favor, insira um valor válido, até 6: "))

if __name__ == '__main__':
    main()