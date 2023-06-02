# Relatório da Sprint 8

Na **Sprint 8**, nosso principal objetivo foi realizar a ingestão de dados das APIs TMDB e OMDB para complementar as informações contidas no arquivo `movies.csv`, armazenado no bucket S3 da AWS. Optamos por essas APIs devido à quantidade abrangente de dados disponíveis. O tema escolhido para o projeto foi *"O impacto dos serviços de streaming na indústria cinematográfica"*. Nosso propósito era analisar a evolução do cinema ao longo das décadas, desde 1900 até os dias atuais, e investigar o impacto dos serviços de streaming nessa indústria.

## Processo de Ingestão de Dados

Para concretizar essa tarefa, utilizamos o **AWS Lambda** para realizar as requisições às APIs. Desenvolvemos duas funções distintas: uma para a API do TMDB e outra para a API do OMDB. Essa abordagem foi adotada devido aos limites diários de requisições impostos por cada API. No total, foram efetuadas cerca de 1300 requisições, em média, para cada uma delas. No caso da API do OMDB, foi necessário dividir as requisições em dois dias, em razão do limite diário de 1000 requisições.

Ao efetuar as requisições, nosso foco recaiu sobre filmes dos gêneros **fantasia** e **ficção científica** que sao os filmes definidos como tema da nossa squad, excluindo aqueles que possuíam múltiplos gêneros, como fantasia e aventura, a fim de garantir maior precisão nos dados coletados.

As **funções Lambda** que desenvolvemos estão localizadas no link abaixo, disponíveis para inspeção e referência. Além disso, durante a **Sprint 8**, também realizamos exercícios envolvendo o **Spark**, aprimorando nossas habilidades nessa área.

[Funcão Lambda OMDB](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/8-Sprint8-Relatorio-Fun%C3%A7%C3%A3oLambda/LambdaDadosOMDB.py)
[Funcao Lambda TMDB](https://github.com/joaoFelipeSales/Programa-Data-Analytics-AWS-CompassUol/blob/main/8-Sprint8-Relatorio-Fun%C3%A7%C3%A3oLambda/LambdaDadosTMDB.py)

## Conclusão

A **Sprint 8** foi concluída com êxito, cumprindo os objetivos propostos de ingestão de dados e preparação do dataset para análise do impacto dos serviços de streaming na indústria cinematográfica.
