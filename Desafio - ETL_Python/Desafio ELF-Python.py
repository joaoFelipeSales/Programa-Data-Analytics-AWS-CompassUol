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

print(dados)

max_num_movies = 0
max_actor = ''

for registro in dados:
    num_movies = int(registro['Number of Movies'])
    if num_movies > max_num_movies:
        max_num_movies = num_movies
        max_actor = registro['Actor']

resultado = "O ator/atriz com o maior número de filmes é {} com um total de {} filmes.".format(max_actor, max_num_movies)

print(resultado)

with open('etapa-1.txt', 'w') as arquivo:
    arquivo.write(resultado)

# 2-Apresente a  média de faturamento bruto por ator.

faturamento_por_ator = {}

for registro in dados:
    actor = registro['Actor']
    gross = float(registro['Total Gross'].replace('$', '').replace(',', ''))
    if actor in faturamento_por_ator:
        faturamento_por_ator[actor]['total'] += gross
        faturamento_por_ator[actor]['filmes'] += 1
    else:
        faturamento_por_ator[actor] = {'total': gross, 'filmes': 1}

resultado = ''
for actor, valores in faturamento_por_ator.items():
    media = valores['total'] / valores['filmes']
    resultado += "A média de faturamento bruto para {} é de ${:,.2f} por filme.\n".format(actor, media)

print(resultado)

with open('etapa-2.txt', 'w') as arquivo:
    arquivo.write(resultado)

# 3-Apresente o ator/atriz com a maior média de faturamento por filme.

media_por_ator = {}
for actor, valores in faturamento_por_ator.items():
    media_por_ator[actor] = valores['total'] / valores['filmes']

ator_mais_lucrativo = max(media_por_ator, key=media_por_ator.get)
media_mais_lucrativa = media_por_ator[ator_mais_lucrativo]

print("O ator/atriz com a maior média de faturamento por filme é {} com uma média de ${:,.2f} por filme.".format(ator_mais_lucrativo, media_mais_lucrativa))

with open('etapa-3.txt', 'w') as arquivo:
    arquivo.write("O ator/atriz com a maior média de faturamento por filme é {} com uma média de ${:,.2f} por filme.".format(ator_mais_lucrativo, media_mais_lucrativa))

# 4-O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

filmes = {}
for registro in dados:
    titulo = registro['#1 Movie']
    if titulo in filmes:
        filmes[titulo] += 1
    else:
        filmes[titulo] = 1

filmes_mais_frequentes = []
frequencia_maxima = max(filmes.values())
for titulo, frequencia in filmes.items():
    if frequencia == frequencia_maxima:
        filmes_mais_frequentes.append(titulo)

if len(filmes_mais_frequentes) > 1:
    print("Os filmes mais frequentes são:", ", ".join(filmes_mais_frequentes), "com", frequencia_maxima, "ocorrências.")
else:
    print("O filme mais frequente é:", filmes_mais_frequentes[0], "com", frequencia_maxima, "ocorrências.")

with open('etapa-4.txt', 'w') as arquivo:
    if len(filmes_mais_frequentes) > 1:
        arquivo.write("Os filmes mais frequentes são: " + ", ".join(filmes_mais_frequentes) + " com " + str(frequencia_maxima) + " ocorrências.")
    else:
        arquivo.write("O filme mais frequente é: " + filmes_mais_frequentes[0] + " com " + str(frequencia_maxima) + " ocorrências.")

# 5-cria um dicionário com o faturamento bruto total de cada ator
faturamento_total = {}
for registro in dados:
    ator = registro['Actor']
    faturamento = float(registro['Total Gross'])
    if ator in faturamento_total:
        faturamento_total[ator] += faturamento
    else:
        faturamento_total[ator] = faturamento

atores_ordenados = sorted(faturamento_total.items(), key=lambda x: x[1], reverse=True)

lista_ordenada = [ator for ator, faturamento in atores_ordenados]
print(f"A lista de atores ordenada pelo faturamento bruto total, em ordem decrescente, é: {lista_ordenada}")

with open('etapa-5.txt', 'w') as arquivo:
    arquivo.write(f"A lista de atores ordenada pelo faturamento bruto total, em ordem decrescente, é: {lista_ordenada}")









