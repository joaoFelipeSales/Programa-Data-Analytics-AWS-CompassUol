import pandas as pd

# carregando o arquivo actors.csv
df = pd.read_csv('actors.csv', header=0, usecols=[0,2])

# contando o número de filmes para cada ator/atriz
num_filmes_por_ator = df.groupby('Actor')['Number of Movies'].sum()

# obtendo o ator/atriz com o maior número de filmes
ator_com_mais_filmes = num_filmes_por_ator.idxmax()
num_filmes_do_ator_com_mais_filmes = num_filmes_por_ator.max()

# exibindo o resultado
print("Ator/atriz com o maior número de filmes:")
print(f"{ator_com_mais_filmes} - {num_filmes_do_ator_com_mais_filmes} filmes")

