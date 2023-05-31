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

# 2-Apresente a  média de faturamento bruto por ator.

total_gross = 0
num_filmes = 0

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
        total_gross += float(registro['Total Gross'].replace('$', '').replace(',', ''))
        num_filmes += 1

media_gross = total_gross / num_filmes

resultado = "A média de ganhos brutos por Ator é ${:,.2f}".format(media_gross)

print(resultado)

with open('etapa-2.txt', 'w') as arquivo:
    arquivo.write(resultado)

# 3 - Apresente o ator/atriz com a maior média de faturamento por filme.

faturamento_por_ator = {}

# Calcula o faturamento total e o número de filmes para cada ator
for registro in dados:
    actor = registro['Actor']
    gross = float(registro['Total Gross'].replace('$', '').replace(',', ''))
    num_movies = int(registro['Number of Movies'])
    if actor in faturamento_por_ator:
        faturamento_por_ator[actor]['total'] += gross
        faturamento_por_ator[actor]['filmes'] += num_movies
    else:
        faturamento_por_ator[actor] = {'total': gross, 'filmes': num_movies}

# Calcula a média de faturamento por filme para cada ator
media_por_ator = {}
for actor, valores in faturamento_por_ator.items():
    media = valores['total'] / valores['filmes']
    media_por_ator[actor] = media

# Encontra o ator com a maior média de faturamento por filme
max_media = 0
max_actor = ''
for actor, media in media_por_ator.items():
    if media > max_media:
        max_media = media
        max_actor = actor

resultado = "O ator/atriz com a maior média de faturamento por filme é {} com ${:,.2f} por filme.".format(max_actor, max_media)

print(resultado)

with open('etapa-3.txt', 'w') as arquivo:
    arquivo.write(resultado)

# 4 - O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

frequencia_filmes = {}

# Conta a frequência de cada nome de filme
for registro in dados:
    filmes = registro['#1 Movie'].split(',')
    for filme in filmes:
        filme = filme.strip()
        if filme in frequencia_filmes:
            frequencia_filmes[filme] += 1
        else:
            frequencia_filmes[filme] = 1

# 4 Encontra o(s) nome(s) de filme(s) com a maior frequência
max_frequencia = 0
filmes_max_frequencia = []
for filme, frequencia in frequencia_filmes.items():
    if frequencia > max_frequencia:
        max_frequencia = frequencia
        filmes_max_frequencia = [filme]
    elif frequencia == max_frequencia:
        filmes_max_frequencia.append(filme)

# Cria a mensagem de saída
if len(filmes_max_frequencia) == 1:
    resultado = "O filme {} com {} frequências.".format(filmes_max_frequencia[0], max_frequencia)

print(resultado)

with open('etapa-4.txt', 'w') as arquivo:
    arquivo.write(resultado)

#5. A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.
faturamento_total = []
for registro in dados:
    actor = registro['Actor']
    gross = float(registro['Total Gross'].replace('$', '').replace(',', ''))
    if any(actor in tupla for tupla in faturamento_total):
        index = next((i for i, tupla in enumerate(faturamento_total) if actor in tupla), None)
        faturamento_total[index] = (actor, faturamento_total[index][1] + gross)
    else:
        faturamento_total.append((actor, gross))

# ordenar lista em ordem decrescente com base no faturamento total
faturamento_total_sorted = sorted(faturamento_total, key=lambda tupla: tupla[1], reverse=True)

# criar string com lista ordenada de nomes de atores
resultado = ''
for tupla in faturamento_total_sorted:
    resultado += "{}\n".format(tupla[0])

print(resultado)

with open('etapa-5.txt', 'w') as arquivo:
    arquivo.write(resultado)