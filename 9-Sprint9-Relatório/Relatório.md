# Relatório da Sprint 9

## Tarefa1: Modelagem Relacional - Normatização

Na tarefa1, que teve como tema "Modelagem Relacional - Normatização", realizei a seguinte normatização (1NF, 2NF, 3NF). [Link para a normatização](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/Tarefa1-Normaliza%C3%A7%C3%A3o.txt).

Com base nessa normatização, criei as seguintes tabelas utilizando o código abaixo no BD Browser (SQLite). Segue o código utilizado para gerar as tabelas e popular elas:

[Código](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/Tarefa1-Modelagem%20Relacional-Normaliza%C3%A7%C3%A3o.sql)

[Modelagem](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/ModelagemLogica.png)

## Tarefa2: Modelagem Dimensional

Na tarefa2, realizamos uma modelagem dimensional. Criei as seguintes views dimensões e a tabela fato que estao nos seguintes links.

[Modelagem Dimencional](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/ModelagemDimensional.png). 

Também incluí a print e código das views.

[Print das views](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/ViewDimensoes.png)
[Código](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/9-Sprint9-Modelagem/Normaliza%C3%A7%C3%A3o/Tarefa2-ModelagemDimensional.sql)

## Tarefa3: Camada Trusted

O objetivo da tarefa 3 era criar a camada "Trusted". Eu fiz a camada "Trusted" a partir do arquivo gerado na sprint anterior. No meu caso, tive que usar duas APIs com muitas requisições, então desenvolvi dois scripts para realizar esse processo. Aqui seguem os links para os scripts: [Trusted-OMDB](link_trusted_omdb) e [Trusted-OMDB](link_trusted_omdb). O arquivo resultante dessas duas etapas foi salvo na camada "Trusted".

## Tarefa 4: Modelagem dos Dados

Na tarefa 4, realizamos a modelagem dos dados para o tema do desafio final. Criei as tabelas no Data Catalog no Glue, resultando nas seguintes tabelas: "Dados-TMDB" e "Dados-OMDB". Aqui está a print das duas tabelas:

![Print das tabelas](link_print_tabelas)

## Tarefa 5: Processamento dos Dados

Na tarefa 5, processamos os dados que serão utilizados, que foram verificados nas etapas anteriores, e os salvamos no formato Parquet na camada "Refined". Seguem os links para os códigos utilizados: [Refined-TMDB](link_refined_tmdb) e [Refined-OMDB](link_refined_omdb).

Esse é o relatório da Sprint 9, com melhorias feitas utilizando a sintaxe Markdown para torná-lo mais legível e organizado.
