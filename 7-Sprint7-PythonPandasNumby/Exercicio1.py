import pandas as pd

# carregando o arquivo
df = pd.read_csv('actors.csv')

# contando o número de filmes para cada ator/atriz
num_filmes_por_ator = df.groupby('Actor')['Number of Movies'].sum()

# obtendo o ator/atriz com o maior número de filmes
ator_com_mais_filmes = num_filmes_por_ator.idxmax()
num_filmes_do_ator_com_mais_filmes = num_filmes_por_ator.max()

print(f"Ator/atriz com o maior número de filmes: {ator_com_mais_filmes} - {num_filmes_do_ator_com_mais_filmes} filmes")

