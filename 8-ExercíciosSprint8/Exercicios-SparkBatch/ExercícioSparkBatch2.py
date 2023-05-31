import csv

# Declaração e inicialização da lista de animais
animais = ['Leão', 'Tigre', 'Girafa', 'Elefante', 'Zebra', 'Cachorro', 'Gato', 'Rato', 'Macaco', 'Coelho',
           'Cavalo', 'Vaca', 'Coruja', 'Pato', 'Galinha', 'Sapo', 'Cobra', 'Tartaruga', 'Pinguim', 'Peixe']

# Ordenar a lista em ordem crescente
animais.sort()

# Iterar sobre os itens e imprimir um a um
[print(animal) for animal in animais]

# Armazenar o conteúdo da lista em um arquivo de texto no formato CSV
with open('animais.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Animal'])  # Escreve o cabeçalho do CSV
    escritor_csv.writerows([[animal] for animal in animais])  # Escreve os animais em cada linha
