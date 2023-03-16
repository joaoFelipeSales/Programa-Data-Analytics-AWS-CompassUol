# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo


def divide_lista(lista):
    tamanho = len(lista)
    terco = tamanho // 3
        
    if tamanho % 3 != 0:
        return None
       
    lista1 = lista[:terco]
    lista2 = lista[terco:terco*2]
    lista3 = lista[terco*2:]
    
    return [lista1, lista2, lista3]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nova_lista = divide_lista(lista)

print(nova_lista) 

 








