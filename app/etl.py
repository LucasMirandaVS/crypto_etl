import requests
import pandas as pd
from sqlalchemy import create_engine

API_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10"

def extract():
    response = requests.get(API_URL)
    data = response.json()
    return pd.DataFrame(data)

def transform(df):
    df = df.loc[:, ["id", "symbol", "current_price", "market_cap"]].copy()  # Cria uma cópia explícita do DataFrame

    # Converte a coluna 'market_cap' para valores numéricos e substitui valores inválidos por zero
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors="coerce").fillna(0).astype(float)

    # Converte o market_cap para bilhões
    df["market_cap"] = df["market_cap"] / 1e9

    return df

def load(df):
    engine = create_engine("postgresql://user:password@db:5432/etl_db")
    df.to_sql("crypto_prices", engine, if_exists="replace", index=False)

def run_etl():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run_etl()
