import requests
import pandas as pd

api_key = "14112cfa08232e0c3fda55940c07e5a6"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=14112cfa08232e0c3fda55940c07e5a6&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df = {
        'Título': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }

    filmes.append(df)

df = pd.DataFrame(filmes)
print(df)
