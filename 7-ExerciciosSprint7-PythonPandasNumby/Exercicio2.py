# Apresente a média da coluna contendo o número de filmes.

import pandas as pd

# carregando o arquivo actors.csv
df = pd.read_csv('actors.csv')

# calculando a média do número de filmes
media_num_filmes = df['Number of Movies'].mean()

# exibindo o resultado
print(f"Média do número de filmes: {media_num_filmes}")

