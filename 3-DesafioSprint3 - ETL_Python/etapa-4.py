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
    resultado = "O filme com mais frequência é {} com {} frequências.".format(filmes_max_frequencia[0], max_frequencia)

print(resultado)

with open('etapa-4.txt', 'w') as arquivo:
    arquivo.write(resultado)