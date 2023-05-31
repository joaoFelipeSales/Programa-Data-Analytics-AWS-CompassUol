# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores. A string deve ter valor  "1,3,4,6,10,76"

def soma_numeros(string_numeros):
    lista_numeros = string_numeros.split(',')
    soma_total = sum(map(int, lista_numeros))
    return soma_total

string_numeros = "1,3,4,6,10,76"
soma_total = soma_numeros(string_numeros)
print(soma_total)