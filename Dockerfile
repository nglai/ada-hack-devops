# Utilize a imagem base do Python 3.10 com Alpine
FROM python:3.11-alpine

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o requirements.txt para o container e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do seu código de aplicação para o container
COPY . /app

# Informe ao Docker que a aplicação roda na porta 8000
EXPOSE 8000

# Comando para rodar a aplicação usando o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
