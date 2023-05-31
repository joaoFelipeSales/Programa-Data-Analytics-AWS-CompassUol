import boto3

s3 = boto3.resource("s3")

bucket_name = "compassuol"

movies_key = "Raw/Local/CSV/Movies/2022/05/02/movies.csv"
series_key = "Raw/Local/CSV/Series/2022/05/02/series.csv"

bucket = s3.Bucket(bucket_name)

bucket.upload_file(Filename="movies.csv", Key=movies_key)
bucket.upload_file(Filename="series.csv", Key=series_key)

