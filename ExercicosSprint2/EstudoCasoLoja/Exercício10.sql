--A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas 
--(quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor 
--está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, 
--calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base
--de dados com status concluído. As colunas presentes no resultado devem ser vendedor, 
--valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente
--arredondado na segunda casa decimal.

SELECT v.nmvdd AS vendedor, 
ROUND(SUM(vi.qtd * vi.vrunt), 2) AS valor_total_vendas, 
ROUND(SUM(vi.qtd * vi.vrunt) * v.perccomissao / 100, 2) AS comissao 
FROM tbvendedor v 
INNER JOIN tbvendas vd ON v.cdvdd = vd.cdvdd 
INNER JOIN tbvendas vi ON vd.cdven = vi.cdven 
WHERE vd.status = 'Concluído' 
GROUP BY v.cdvdd 
ORDER BY comissao DESC;
