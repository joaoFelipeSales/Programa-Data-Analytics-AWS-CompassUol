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

# Caminho dos arquivos no S3
input_path = "s3://compassuol/Raw/TMDB/JSON/2023/05/30/"

# Definir o esquema dos arquivos JSON
schema = StructType([
    StructField("adult", BooleanType(), nullable=True),
    StructField("backdrop_path", StringType(), nullable=True),
    StructField("belongs_to_collection", StringType(), nullable=True),
    StructField("budget", IntegerType(), nullable=True),
    StructField("homepage", StringType(), nullable=True),
    StructField("id", IntegerType(), nullable=True),
    StructField("imdb_id", StringType(), nullable=True),
    StructField("original_language", StringType(), nullable=True),
    StructField("original_title", StringType(), nullable=True),
    StructField("overview", StringType(), nullable=True),
    StructField("popularity", FloatType(), nullable=True),
    StructField("poster_path", StringType(), nullable=True),
    StructField("release_date", StringType(), nullable=True),
    StructField("revenue", IntegerType(), nullable=True),
    StructField("runtime", IntegerType(), nullable=True),
    StructField("status", StringType(), nullable=True),
    StructField("tagline", StringType(), nullable=True),
    StructField("title", StringType(), nullable=True),
    StructField("video", BooleanType(), nullable=True),
    StructField("vote_average", FloatType(), nullable=True),
    StructField("vote_count", IntegerType(), nullable=True)
])

# Ler os arquivos JSON com o esquema especificado
dataframe1 = spark.read.schema(schema).json(input_path + "filtered_movies_TMDB_FANTASY.json")
dataframe2 = spark.read.schema(schema).json(input_path + "filtered_movies_TMDB_SCI-FI.json")

# Faz a união dos dataframes
merged_dataframe = dataframe1.union(dataframe2)


merged_dataframe = merged_dataframe.coalesce(1)

# Salva o dataframe resultante como arquivo Parquet
output_path = "s3://compassuol/Raw/Trusted/TMDB_FANTASY+SCI-FI.parquet"
merged_dataframe.write.parquet(output_path)

# Finaliza o job
job.commit()