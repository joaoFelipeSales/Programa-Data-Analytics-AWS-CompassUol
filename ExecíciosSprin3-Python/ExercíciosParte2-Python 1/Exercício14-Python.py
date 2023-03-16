# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número 
# variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
# Teste sua função com os seguintes parâmetros: (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

def print_params(*args, **kwargs):
    print("Parâmetros não nomeados:")
    for arg in args:
        print(arg)
    print("Parâmetros nomeados:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_params(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

