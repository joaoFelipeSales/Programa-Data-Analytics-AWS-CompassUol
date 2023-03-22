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