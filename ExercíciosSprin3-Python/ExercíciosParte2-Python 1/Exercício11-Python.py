""" Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo."""


arquivo = open('arquivo_texto.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()









