--Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

SELECT DISTINCT nome
FROM autor
WHERE codautor not in (SELECT autor from livro)
ORDER by nome
