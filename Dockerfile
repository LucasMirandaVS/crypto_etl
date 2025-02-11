# Usar uma imagem base do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências do sistema necessárias para o psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de dependências
COPY pyproject.toml poetry.lock ./

# Instalar o Poetry e as dependências do projeto
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copiar o restante do código
COPY . .

# Comando padrão para executar o ETL
CMD ["python", "app/main.py"]