FROM python:3.9

WORKDIR /app

COPY . .

# Define as variáveis de ambiente para as credenciais da AWS
ENV AWS_ACCESS_KEY_ID=AKIA2EMGRSC5WJ6KGCW2
ENV AWS_SECRET_ACCESS_KEY=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

RUN pip install -r requirements.txt

CMD [ "python", "codigo.py" ]
