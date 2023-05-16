FROM python:3.9

WORKDIR /app

COPY . /app

# Define as variáveis de ambiente para as credenciais da AWS
ENV AWS_ACCESS_KEY_ID=AKIA2EMGRSC5ZLGFBWQI
ENV AWS_SECRET_ACCESS_KEY=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

RUN pip install -r requirements.txt

CMD [ "python", "codigo.py" ]
