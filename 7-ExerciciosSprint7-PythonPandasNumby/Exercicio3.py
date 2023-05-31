# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

# Carrega o arquivo CSV com os dados dos atores e atrizes
df = pd.read_csv('actors.csv')

# Agrupa os dados pelo nome do ator/atriz e calcula a média por filme
media_por_ator = df.groupby('Actor')['Average per Movie'].mean()

# Obtém o nome do ator/atriz com a maior média por filme
ator_com_media_mais_alta = media_por_ator.idxmax()

# Imprime o resultado
print(ator_com_media_mais_alta)
