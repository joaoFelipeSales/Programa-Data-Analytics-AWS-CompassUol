--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas
--na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes
--repetidos em seu retorno.


SELECT DISTINCT autor.nome
FROM autor
left JOIN livro ON livro.autor = codautor
left JOIN editora ON livro.editora = codeditora
left JOIN endereco ON editora.endereco = codendereco
WHERE estado not in ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
ORDER BY autor.nome ASC;