import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, IntegerType, ArrayType, FloatType, DateType

# Obtém os argumentos e o nome do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job_name = args['JOB_NAME']

# Inicializa o contexto do Glue e o SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(job_name, args)

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

# Ler o arquivo Parquet
input_path = "s3://compassuol/Raw/Trusted/OMDB_FANTASY+SCI-FI.parquet/"
df = spark.read.parquet(input_path)

# Selecionar apenas as colunas desejadas
selected_columns = ["imdbID", "Title", "Year", "BoxOffice", "imdbRating", "imdbVotes", "Rated"]
df_selected = df.select(*selected_columns)

# Escrever o resultado em um novo arquivo Parquet
output_path = "s3://compassuol/Raw/REFINED/OMDB"
df_selected.write.parquet(output_path)

job.commit()