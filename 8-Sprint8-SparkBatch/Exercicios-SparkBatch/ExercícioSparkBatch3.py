import random
import time
import os
import names

# Define a semente de aleatoriedade
random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gerar os nomes aleatórios
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Gerar um arquivo de texto contendo todos os nomes
arquivo = "nomes_aleatorios.txt"
with open(arquivo, "w") as file:
    for nome in dados:
        file.write(nome + "\n")

# Verificar o conteúdo do arquivo
os.system("notepad.exe " + arquivo)
