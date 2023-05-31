--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela 
--coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade 
--(total de livros de sua autoria).


SELECT nome, codautor, nascimento, COUNT(livro.autor) AS quantidade
FROM autor 
    left JOIN livro ON autor.codautor = livro.autor
GROUP BY nome, nascimento, codautor
ORDER BY autor.nome 