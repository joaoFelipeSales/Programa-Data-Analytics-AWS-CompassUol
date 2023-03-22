# 1-Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
dados = []

with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    cabecalho = linhas[0].strip().split(',')
    for linha in linhas[1:]:
        valores = []
        valor = ""
        entre_aspas = False
        for i in range(len(linha)):
            if linha[i] == ',' and not entre_aspas:
                valores.append(valor.strip())
                valor = ""
            elif linha[i] == '"':
                entre_aspas = not entre_aspas
            else:
                valor += linha[i]
        valores.append(valor.strip())
        registro = {}
        for i in range(len(cabecalho)):
            registro[cabecalho[i]] = valores[i]
        dados.append(registro)

max_num_movies = 0
max_actor = ''

for registro in dados:
    num_movies = int(registro['Number of Movies'])
    if num_movies > max_num_movies:
        max_num_movies = num_movies
        max_actor = registro['Actor']

resultado = "O ator/atriz com o maior número de filmes é {} com {} filmes.".format(max_actor, max_num_movies)

print(resultado)