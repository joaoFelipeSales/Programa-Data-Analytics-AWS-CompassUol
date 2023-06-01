import boto3
import csv
import requests
import json

def lambda_handler(event, context):
    # Nome do seu bucket no Amazon S3
    bucket_name = 'compassuol'
    
    # Nome do arquivo no bucket
    file_name = 'movies.csv'
    
    # Nome do arquivo JSON para salvar as informações dos IDs filtrados
    output_file_name = 'filtered_movies_OMDB_Sci-Fi.json'
    
    # Diretório no Amazon S3 para salvar o arquivo JSON
    directory_name = 'Raw/OMDB/JSON/2023/05/30/'
    
    # Criar uma instância do cliente do S3
    s3 = boto3.client('s3')
    
    try:
        # Fazer o download do arquivo do S3
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = response['Body'].read().decode('utf-8')
        
        # Filtrar os IDs dos filmes com gênero "Fantasia" (sem duplicatas)
        filtered_ids = set()
        
        reader = csv.DictReader(content.splitlines(), delimiter='|')
        for row in reader:
            if row['genero'] == 'Sci-Fi':
                filtered_ids.add(row['id'])
        
        # Fazer a requisição à API do OMDB para obter os dados dos filmes
        movie_data = []
        for movie_id in filtered_ids:
            # Substitua 'API_KEY' pela sua chave de API do OMDB
            url = f'https://www.omdbapi.com/?i={movie_id}&apikey=2c8c4702&language=pt-BR'
            
            response = requests.get(url)
            if response.status_code == 200:
                movie_data.append(response.json())
        
        # Salvar os dados dos filmes em um arquivo JSON
        json_data = json.dumps(movie_data)
        
        # Definir o caminho completo para o arquivo JSON no S3
        file_path = directory_name + output_file_name
        
        # Fazer upload do arquivo JSON resultante para o S3
        s3.put_object(Body=json_data, Bucket=bucket_name, Key=file_path)
        
        # Retornar código de sucesso
        return {
            'statusCode': 200
        }
    
    except Exception as e:
        # Retornar um erro em caso de falha
        return {
            'statusCode': 500,
            'body': str(e)
        }
