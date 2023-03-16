# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo


def divide_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3  # tamanho de cada parte
    sobra = tamanho % 3  # sobra de elementos para distribuir nas partes
    partes = [lista[i*tamanho_parte:(i+1)*tamanho_parte+sobra] for i in range(3)]
    return partes
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes = divide_lista(lista)
print(partes)

