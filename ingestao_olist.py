import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Configurações de Conexão com o PostgreSQL
DB_USER = "postgres"
DB_PASS = "postgres"  # <--- Coloque a sua senha aqui
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "olist_db"

# String de conexão SQLAlchemy para PostgreSQL
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

try:
    print("Conectando ao banco de dados PostgreSQL...")
    engine = create_engine(DATABASE_URL)
    print("Conexão estabelecida com sucesso!\n")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()

# 2. Mapeamento de arquivos CSV para nomes das tabelas no Banco
arquivos_olist = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "product_category_translation",
}

# 3. Loop de Ingestão
print("--- Iniciando Carga de Dados no PostgreSQL ---")

for arquivo_csv, nome_tabela in arquivos_olist.items():
    if os.path.exists(arquivo_csv):
        print(f"Lendo arquivo: {arquivo_csv} ...")
        df = pd.read_csv(arquivo_csv)

        print(f"Inserindo {len(df)} linhas na tabela '{nome_tabela}'...")
        df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
        print(f"Tabela '{nome_tabela}' carregada com sucesso!\n")
    else:
        print(f"Aviso: Arquivo {arquivo_csv} não foi encontrado na pasta.\n")

print("--- Ingestão concluída com sucesso! ---")
