# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.


with open("arquivo_texto.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)





