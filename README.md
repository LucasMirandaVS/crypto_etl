# ETL Docker Project

Este projeto implementa um pipeline de ETL para coletar dados de criptomoedas da API do CoinGecko e armazená-los em um banco de dados PostgreSQL. A aplicação roda dentro de um container Docker, que é orquestrado com o Docker Compose. A aplicação realiza as seguintes etapas:

1. **Extração (Extract):** A aplicação consulta a API do CoinGecko e coleta informações sobre as principais criptomoedas, como o ID, símbolo, preço atual e capitalização de mercado.
2. **Transformação (Transform):** Os dados coletados são transformados para uma unidade mais legível (capitalização de mercado convertida para bilhões).
3. **Carregamento (Load):** Os dados transformados são armazenados em uma tabela `crypto_prices` em um banco de dados PostgreSQL.

A aplicação e o banco de dados são executados dentro de containers Docker, usando o Docker Compose para orquestração.

## Tecnologias Usadas

- **Python** (para o script ETL)
- **Pandas** (para manipulação de dados)
- **Requests** (para consumir a API)
- **SQLAlchemy** (para interagir com o PostgreSQL)
- **PostgreSQL** (banco de dados relacional)
- **Docker** (para containers)
- **Docker Compose** (para orquestração dos containers)

## Pré-requisitos
- [Docker]
- [Docker Compose]
- [Python 3.12]

## Como Rodar o Projeto

### 1. Clone o Repositório
```bash
git clone <URL-do-repositório>
cd <diretório-do-repositório>
```

### 2. Instalar as Dependências com o Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

### 3. Rodando o Projeto
```bash
docker-compose up --build
docker ps
```

### 4. Acessando o Banco de Dados
```bash
docker exec -it postgres_db psql -U user -d etl_db
```

A partir daí, é possível rodar consultas, como:
```bash
SELECT * FROM crypto_prices;
```