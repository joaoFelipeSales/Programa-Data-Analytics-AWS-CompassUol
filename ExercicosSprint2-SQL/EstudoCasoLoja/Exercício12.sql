--Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com 
--menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser 
--cddep, nmdep, dtnasc e valor_total_vendas. Observação: Apenas vendas com status concluído.


SELECT cddep, nmdep, dtnasc, SUM(qtd * vrunt) as valor_total_vendas
FROM tbdependente  d
JOIN tbvendedor vnd ON vnd.cdvdd = d.cdvdd
JOIN tbvendas v ON v.cdvdd = vnd.cdvdd
WHERE vnd.nmvdd > 0 AND status = 'Concluído'
GROUP BY d.cddep, d.nmdep, d.dtnasc
ORDER BY valor_total_vendas ASC
limit 1;