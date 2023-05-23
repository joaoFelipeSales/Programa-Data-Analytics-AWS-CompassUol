import random

# Declarar uma lista vazia
minha_lista = []

# Gerar 250 números inteiros aleatórios e adicioná-los à lista
for _ in range(250):
    minha_lista.append(random.randint(1, 100))

# Reverter a lista
minha_lista.reverse()

# Imprimir a lista invertida
print(minha_lista)
