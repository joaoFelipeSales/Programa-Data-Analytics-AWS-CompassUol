--Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
--e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, 
--portanto, cdvdd e nmvdd.

SELECT V.cdvdd, V.nmvdd 
FROM (SELECT V.cdvdd, V.nmvdd, COUNT(V.cdvdd) AS qtde 
      FROM tbvendedor AS V
      JOIN tbvendas AS VE ON VE.cdvdd = V.cdvdd 
      WHERE VE.status = 'Concluído'
      GROUP BY V.cdvdd) AS V 
ORDER By V.qtde DESC
LIMIT 1;