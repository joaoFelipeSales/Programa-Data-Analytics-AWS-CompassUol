import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType

# Obtém os argumentos e o nome do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
nome_job = args['JOB_NAME']

# Inicializa o contexto do Glue e o SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(nome_job, args)

# Caminho dos arquivos no S3
caminho_entrada = "s3://compassuol/Raw/OMDB/JSON/2023/05/30/"

# Define o esquema dos arquivos JSON
esquema = StructType([
    StructField("Title", StringType(), nullable=True),
    StructField("Year", StringType(), nullable=True),
    StructField("Rated", StringType(), nullable=True),
    StructField("Released", StringType(), nullable=True),
    StructField("Runtime", StringType(), nullable=True),
    StructField("Genre", StringType(), nullable=True),
    StructField("Director", StringType(), nullable=True),
    StructField("Writer", StringType(), nullable=True),
    StructField("Actors", StringType(), nullable=True),
    StructField("Plot", StringType(), nullable=True),
    StructField("Language", StringType(), nullable=True),
    StructField("Country", StringType(), nullable=True),
    StructField("Awards", StringType(), nullable=True),
    StructField("Poster", StringType(), nullable=True),
    StructField("Metascore", StringType(), nullable=True),
    StructField("imdbRating", StringType(), nullable=True),
    StructField("imdbVotes", StringType(), nullable=True),
    StructField("imdbID", StringType(), nullable=True),
    StructField("Type", StringType(), nullable=True),
    StructField("DVD", StringType(), nullable=True),
    StructField("BoxOffice", StringType(), nullable=True),
    StructField("Production", StringType(), nullable=True),
    StructField("Website", StringType(), nullable=True),
    StructField("Response", StringType(), nullable=True)
])

# Lê os arquivos JSON com o esquema especificado
dataframe1 = spark.read.schema(esquema).json(caminho_entrada + "filtered_movies_OMDB_FANTASY.json")
dataframe2 = spark.read.schema(esquema).json(caminho_entrada + "filtered_movies_OMDB_Sci-Fi.json")

# Realiza a união dos dataframes
dataframe_mesclado = dataframe1.union(dataframe2)

dataframe_mesclado = dataframe_mesclado.coalesce(1)

# Salva o dataframe resultante como arquivo Parquet
caminho_saida = "s3://compassuol/Raw/Trusted/OMDB_FANTASY+SCI-FI.parquet"
dataframe_mesclado.write.parquet(caminho_saida)

# Finaliza o job
job.commit()

