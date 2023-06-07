CREATE TABLE "tb_clientes" (
	"idCliente" int PRIMARY KEY,
	"nomeCliente" varchar(100),
	"cidadeCliente" varchar(40),
	"estadoCliente" varchar(40),
	"paisCliente" varchar(40)
);
CREATE TABLE "tb_carro" (
	"idCarro" int PRIMARY KEY,
	"classiCarro" varchar(50),
	"marcaCarro" varchar(80),
	"modeloCarro" varchar(80),
	"anoCarro" int,
	"idCombustivel" int,
	FOREIGN KEY ("idCombustivel") REFERENCES "tb_combustivel" ("idCombustivel")
);
CREATE TABLE "tb_combustivel" (
	"idCombustivel" int PRIMARY KEY,
	"tipoCombustivel" varchar(20)
);
CREATE TABLE "tb_vendedor" (
	"idVendedor" int PRIMARY KEY,
	"nomeVendedor" varchar(15),
	"sexoVendedor" smallint,
	"estadoVendedor" varchar(40)
)   

CREATE TABLE "tb_locacao" (
	"idLocacao"	int,
	"idCliente"	int,
	"idCarro"	int,
	"idVendedor"	int,
	"dataLocacao"	datetime,
	"horaLocacao"	time,
	"qtdDiaria"	int,
	"vlrDiaria"	decimal(18, 2),
	"dataEntrega"	date,
	"horaEntrega"	time,
	"kmCarro"	int,
	PRIMARY KEY("idLocacao"),
	FOREIGN KEY("idVendedor") REFERENCES "tb_vendedor"("idVendedor"),
	FOREIGN KEY("idCarro") REFERENCES "tb_carro"("idCarro"),
	FOREIGN KEY("idCliente") REFERENCES "tb_clientes"("idCliente")
);

INSERT INTO "tb_clientes" ("idCliente", "nomeCliente", "cidadeCliente", "estadoCliente", "paisCliente")
SELECT DISTINCT "idCliente", "nomeCliente", "cidadeCliente", "estadoCliente", "paisCliente"
FROM "tb_locacao";


INSERT INTO "tb_combustivel" ("idCombustivel", "tipoCombustivel")
SELECT DISTINCT "idCombustivel", "tipoCombustivel"
FROM "tb_locacao";


INSERT INTO "tb_carro" ("idCarro", "kmCarro", "classiCarro", "marcaCarro", "modeloCarro", "anoCarro", "idCombustivel")
SELECT DISTINCT "idCarro", "kmCarro", "classiCarro", "marcaCarro", "modeloCarro", "anoCarro", "idCombustivel"
FROM "tb_locacao";

INSERT INTO "tb_vendedor" ("idVendedor", "nomeVendedor", "sexoVendedor", "estadoVendedor")
SELECT DISTINCT "idVendedor", "nomeVendedor", "sexoVendedor", "estadoVendedor"
FROM "tb_locacao";


INSERT INTO "tb_locacaonova" (
    "idLocacao", "idCliente", "idCarro", "idVendedor", 
    "dataLocacao", "horaLocacao", "qtdDiaria", "vlrDiaria",
    "dataEntrega", "horaEntrega"
)
SELECT DISTINCT 
    "idLocacao", "idCliente", "idCarro", "idVendedor", 
    "dataLocacao", "horaLocacao", "qtdDiaria", "vlrDiaria",
    "dataEntrega", "horaEntrega"
FROM "tb_locacao";
