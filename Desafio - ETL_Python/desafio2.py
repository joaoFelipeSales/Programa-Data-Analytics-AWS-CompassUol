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

resultado = "A média de ganhos brutos por filme é ${:,.2f}".format(media_gross)

print(resultado)

with open('etapa-3.txt', 'w') as arquivo:
    arquivo.write(resultado)


num_filmes_por_autor = {}

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
        autor = valores[0]
        num_filmes = int(valores[2])
        if autor in num_filmes_por_autor:
            num_filmes_por_autor[autor]['total'] += num_filmes
            num_filmes_por_autor[autor]['filmes'] += 1
        else:
            num_filmes_por_autor[autor] = {'total': num_filmes, 'filmes': 1}

media_filmes_por_autor = sum(d['total'] for d in num_filmes_por_autor.values()) / sum(d['filmes'] for d in num_filmes_por_autor.values())

resultado = "A média de número de filmes por ator é {:.2f}".format(media_filmes_por_autor)

print(resultado)

with open('etapa-4.txt', 'w') as arquivo:
    arquivo.write(resultado)
