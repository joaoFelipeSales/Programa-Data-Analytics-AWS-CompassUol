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