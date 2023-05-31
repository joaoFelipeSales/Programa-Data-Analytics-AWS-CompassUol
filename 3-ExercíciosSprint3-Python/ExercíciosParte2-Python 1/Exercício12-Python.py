"""Leia o arquivo person.json, faça o parsing e imprima seu conteúdo."""

import json

with open('person.json', 'r') as f:
    person = json.load(f)

print(person)