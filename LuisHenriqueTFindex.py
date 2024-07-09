#Trabalho Final: Algoritmos e Programação de Computadores 2
#Nome: Luis Henrique de Melo Santiago
#Turma: BSI23

import funcao1
funcao2, funcao3, funcao4, funcao5, funcao6

start = print("Bem vindo ao software de análise dos dados de...")
Funcoes = print("""Função 1 = Tecla 1; \nFunção 2 = Tecla 2; \nFunção 3 = Tecla 3; \nFunção 4 = Tecla 4; \nFunção 5 = Tecla 5; \nFunção 6 = Tecla 6; \nSair = 0.""" )

def inicio(n):
        while True:
            if n == 1:
                print("Iniciando a função 1.")
                funcao1.funcao_um()
                break

            elif n == 2:
                print("Iniciando a função 2.")
                nomefuncao = input("Insira um nome para a função a ser criada: ")
                with open (f"{nomefuncao}.txt", "w") as newarch:
                    func2 = int(input("Selecione uma função: Função 1 = Tecla 1; \nFunção 2 = Tecla 2; \nFunção 3 = Tecla 3; \n:" ))
                    if func2 == 1:
                        funcao1()
                    elif func2 == 2:
                        newarch()
                    elif func2 == 3:
                        print("função de filtragem de dados")
            
            elif n == 3:
                print("Iniciando a função 3. - Resumo")
                funcao3(c)
            
            elif n == 4:
                print("Iniciando a função 4. - Estatística")
                funcao4(d)
            
            elif n == 5:
                print("Iniciando a função 5. - busca de dados no arquivo")
                funcao5(e)
            
            elif n == 6:
                print("Iniciando a função 6.")
                funcao6(f)
            
            elif n == 0:
                print('Obrigado por usar o programa.')
                return
            else:
                print("Não compreendi.")
            n = int(input("Por favor, insira um valor válido, até 6: "))
n = int(input("Por favor, insira um valor válido, até 6: "))
inicio(n)