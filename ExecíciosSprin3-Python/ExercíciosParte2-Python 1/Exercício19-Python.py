# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: 
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada! 

import random

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

# ordena a lista
random_list.sort()

# calcula o valor mínimo
valor_minimo = random_list[0]

# calcula o valor máximo
valor_maximo = random_list[-1]

# calcula o valor médio
media = sum(random_list) / len(random_list)

# calcula a mediana
if len(random_list) % 2 == 0:
    # se a lista tem um número par de elementos, a mediana é a média dos dois valores centrais
    mediana = (random_list[len(random_list)//2 - 1] + random_list[len(random_list)//2]) / 2
else:
    # se a lista tem um número ímpar de elementos, a mediana é o valor central
    mediana = random_list[len(random_list)//2]

# exibe os resultados
print("Valor mínimo:", valor_minimo)
print("Valor máximo:", valor_maximo)
print("Media:", media)
print("Mediana:", mediana)

