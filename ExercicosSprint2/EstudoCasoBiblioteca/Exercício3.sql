 --Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas 
 --as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade 
 --de livros em ordem decrescente.

select DISTINCT
	count(editora) as quantidade,
	editora.nome, 
	endereco.estado, 
	endereco.cidade
FROM livro
LEFT join editora	
	ON editora = codeditora
left join endereco
	on endereco = codendereco
	
GROUP by cidade
limit 5