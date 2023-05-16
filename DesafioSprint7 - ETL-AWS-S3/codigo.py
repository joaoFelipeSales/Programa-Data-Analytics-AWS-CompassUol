import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket("compassuol")

bucket.upload_file(Key="movies.csv", Filename="movies.csv")
bucket.upload_file(Key="series.csv", Filename="series.csv")
