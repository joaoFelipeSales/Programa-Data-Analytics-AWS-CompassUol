# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: 
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada! 
import random 
random_list = random.sample(range(500),50)
# Use as variáveis abaixo para representar cada operação matemática
# mediana/media/valor_minimo/valor_maximo 

# ordena a lista
random_list.sort()

# calcula o valor mínimo
valor_minimo = random_list[0]

# calcula o valor máximo
valor_maximo = random_list[-1]

# calcula a mediana
n = len(random_list)
if n % 2 == 0:
    mediana = (random_list[n // 2 - 1] + random_list[n // 2]) / 2
else:
    mediana = random_list[n // 2]

# calcula a média
media = sum(random_list) / len(random_list)

# exibe os resultados
print("Valor mínimo: ", valor_minimo)
print("Valor máximo: ", valor_maximo)
print("Mediana: ", mediana)
print("Média: ", media)