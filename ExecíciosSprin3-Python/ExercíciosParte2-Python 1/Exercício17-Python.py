""" Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
    a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo """


def dividir_em_tres_partes(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte:2*tamanho_parte]
    parte3 = lista[2*tamanho_parte:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_em_tres_partes(lista)
print(parte1, parte2, parte3) 




 








