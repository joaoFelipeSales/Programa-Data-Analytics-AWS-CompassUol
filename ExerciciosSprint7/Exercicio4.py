# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

# carregando o arquivo actors.csv
df = pd.read_csv('actors.csv')

# contando a frequência de cada filme
frequencia_por_filme = df['#1 Movie'].value_counts()

# exibindo o resultado
print("Ranking dos filmes de acordo com a frequência no dataset:\n")
for i, (filme, frequencia) in enumerate(frequencia_por_filme.items(), 1):
    print(f"{i} - O filme {filme} aparece {frequencia} vez(es) no dataset")




