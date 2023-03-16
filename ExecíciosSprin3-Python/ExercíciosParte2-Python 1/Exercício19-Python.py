# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: 
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada! 

import numbers as np
import random

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

# ordena a lista
random_list_sorted = sorted(random_list)

# calcula a mediana
mediana = np.median(random_list_sorted)

# calcula a média
media = np.mean(random_list)

# encontra o valor mínimo e máximo
valor_minimo = min(random_list)
valor_maximo = max(random_list)

# imprime os resultados
print("Mediana:", mediana)
print("Média:", media)
print("Valor mínimo:", valor_minimo)
print("Valor máximo:", valor_maximo)

