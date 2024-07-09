#Converte o arquivo para matriz 
import csv
import pandas as pd

def funcao_um():
  arq = "D:\\Sistemas de Informação\\2º Período\\Algoritmos e Programação de Computadores II\\Trabalho final\\arrecadacao-estado.csv"

#Abrindo para leitura do arquivo
  with open (arq, 'r', encoding='ISO-8859-1') as arrec:
    leitor_csv = csv.reader(arrec) #biblioteca para ler csv
    matriz = []
    list_to_str = []

#Transformando o arquivo numa matriz com linhas
    for linha in leitor_csv:
      matriz.append(linha)
    print(f"Temos {len(matriz)} linhas na matriz de arrecadação por estado, contando com o cabeçalho.")

#Transformando a primeira linha numa lista para ser apresentado
    for item in matriz[0]:
      campos = item.split(';')
      list_to_str.append(campos)
  print(list_to_str[0])



