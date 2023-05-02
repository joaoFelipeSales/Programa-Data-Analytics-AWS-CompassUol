# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

# carregando o arquivo actors.csv
df = pd.read_csv('actors.csv')

# calculando a média do número de filmes para cada ator/atriz
media_num_filmes_por_ator = df.groupby('Actor')['Number of Movies'].mean()

# obtendo o ator/atriz com a maior média por filme
ator_com_maior_media = media_num_filmes_por_ator.idxmax()
maior_media_num_filmes = media_num_filmes_por_ator.max()

# exibindo o resultado
print(f"Ator/atriz com a maior média por filme: {ator_com_maior_media} - {maior_media_num_filmes:.2f} filmes por ano")
