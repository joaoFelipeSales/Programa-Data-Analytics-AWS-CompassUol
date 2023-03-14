# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

# Abre o arquivo person.json e faz o parsing do conteúdo em um dicionário Python
with open('person.json', 'r') as f:
    person = json.load(f)

# Imprime o conteúdo do dicionário
print(person)