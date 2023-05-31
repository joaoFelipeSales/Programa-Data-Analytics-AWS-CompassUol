""" Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: 
    Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada! """

import random

random_list = random.sample(range(500),50)

random_list.sort()

valor_minimo = random_list[0]

valor_maximo = random_list[-1]

media = sum(random_list) / len(random_list)

if len(random_list) % 2 == 0:
    mediana = (random_list[len(random_list)//2 - 1] + random_list[len(random_list)//2]) / 2
else:
    mediana = random_list[len(random_list)//2],
    
print("Media:", media, end=", ")
print("Mediana:", mediana, end=", ")
print("Mínimo:", valor_minimo, end=", ")
print("Máximo:", valor_maximo)

