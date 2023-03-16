# Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
# Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
# Exemplo: 0 - João Soares está com 19 anos

for i, (primeiroNome, sobreNome) in enumerate(zip(primeirosNomes, sobreNomes)):
    idade = idades[i]
    print(f"{i} - {primeiroNome} {sobreNome} está com {idade} anos")
