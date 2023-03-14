# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def divide_lista(lista):
    tamanho = len(lista)
    terco = tamanho // 3
    return lista[:terco], lista[terco:2*terco], lista[2*terco:]

parte1, parte2, parte3 = divide_lista(lista)
print(parte1)  # [1, 2, 3, 4]
print(parte2)  # [5, 6, 7, 8]
print(parte3)  # [9, 10, 11, 12]