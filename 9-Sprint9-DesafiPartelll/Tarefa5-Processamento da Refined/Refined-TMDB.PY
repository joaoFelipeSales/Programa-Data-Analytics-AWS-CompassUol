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

# Ler o arquivo Parquet
input_path = "s3://compassuol/Raw/Trusted/TMDB_FANTASY+SCI-FI.parquet/"
df = spark.read.parquet(input_path)

# Selecionar apenas as colunas desejadas
selected_columns = ["imdb_id", "title", "release_date", "revenue", "budget", "popularity"]
df_selected = df.select(*selected_columns)

# Escrever o resultado em um novo arquivo Parquet
output_path = "s3://compassuol/Raw/REFINED/TMDB"
df_selected.write.parquet(output_path)

job.commit()