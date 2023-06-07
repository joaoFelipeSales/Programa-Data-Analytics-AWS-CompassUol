-- View Dimensão Cliente
CREATE VIEW dim_cliente AS
SELECT
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM
    tb_locacao;

-- View Dimensão Carro
CREATE VIEW dim_carro AS
SELECT
    idCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idcombustivel
FROM
    tb_locacao;

-- View Dimensão Localidade
CREATE VIEW dim_localidade AS
SELECT DISTINCT
    cidadeCliente AS cidade,
    estadoCliente AS estado,
    paisCliente AS país
FROM
    tb_locacao;

-- View Dimensão Data
CREATE VIEW dim_data AS
SELECT DISTINCT
    dataLocacao AS data,
    horaLocacao AS hora
FROM
    tb_locacao;

-- View Fato Locação
CREATE VIEW fato_locacao AS
SELECT
    idLocacao,
    idCliente,
    idCarro,
    qtdDiaria,
    vlrDiaria
FROM
    tb_locacao;