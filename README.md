[README.md](https://github.com/user-attachments/files/33127948/README.md)
# Olist E-commerce Analytics

![Dashboard Preview](./assets/Captura%20de%20tela%202026-10-06%20171315.png)

Projeto de analytics end-to-end para o dataset público de e-commerce da Olist, com foco em extração, tratamento, modelagem e visualização de dados de vendas para apoio à tomada de decisão.

## Visão Geral

Este repositório reúne a base de dados, os scripts de ingestão, a modelagem em SQL e o dashboard em Power BI para transformar o dataset da Olist em uma solução analítica pronta para exploração de KPIs e insights de negócio.

## Objetivo do Projeto

Responder perguntas estratégicas como:

- Qual o faturamento total da operação?
- Quantos pedidos foram concluídos no período?
- Qual o ticket médio por pedido?
- Como o frete impacta a rentabilidade?
- Quais regiões e categorias performam melhor?
- Como as vendas evoluem ao longo do tempo?

## Stack Tecnológica

- Python: ingestão e carga dos CSVs para o banco
- Pandas: leitura e transformação dos dados
- SQLAlchemy: conexão com PostgreSQL
- PostgreSQL: armazenamento e modelagem analítica
- Power BI: visualização, KPIs e dashboard executivo

## Arquitetura do Pipeline

```text
Kaggle (CSV)
   ↓
Python (ingestão)
   ↓
PostgreSQL
   ↓
View analítica (SQL)
   ↓
Power BI (dashboard)
```

## Estrutura do Repositório

```text
olist-ecommerce-analytics/
├── Dashboard/
│   └── Dashboard_Vendas_Olist.pbix
├── Scripts/
│   ├── README.MD
│   ├── ingestao_olist.py
│   └── vw_vendas.sql
├── data/
│   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   ├── product_category_name_translation.csv
│   └── olist_geolocation_dataset.csv
└── README.md (opcional, caso queira criar um README principal da raiz)
```

## Dados

Fonte dos dados: dataset público da Olist Brazilian E-Commerce, disponibilizado no Kaggle.

## KPIs e Métricas Monitoradas

- Faturamento total
- Total de pedidos
- Ticket médio
- Total de frete
- Evolução de vendas por mês
- Performance por região e categoria

## Insights de Negócio

- Região Sudeste concentra a maior parte do faturamento
- São Paulo se destaca como principal estado da operação
- Categorias como Beleza & Saúde e Relógios & Presentes apresentam forte contribuição
- Há crescimento consistente de vendas em 2017 e 2018, com tendência sazonal no fim do ano

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

- Python 3.x instalado
- PostgreSQL instalado e em execução
- pgAdmin 4 ou cliente SQL para executar views e consultas
- Power BI Desktop
- Dataset da Olist baixado e disponibilizado na pasta `data/`

## Como Replicar o Projeto

### 1. Clone o repositório

```bash
git clone <https://github.com/Hudson-hag/olist-ecommerce-analytics.git>
cd olist-ecommerce-analytics
```

### 2. Prepare o banco de dados

Crie um banco PostgreSQL, por exemplo:

```sql
CREATE DATABASE olist_db;
```

### 3. Instale as dependências Python

```bash
pip install pandas sqlalchemy psycopg2-binary
```

### 4. Ajuste as credenciais de conexão

No arquivo `Scripts/ingestao_olist.py`, configure usuário, senha, host, porta e nome do banco conforme o ambiente local:

```python
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "olist_db"
```

### 5. Execute a ingestão

Acesse a pasta do projeto e rode:

```bash
python Scripts/ingestao_olist.py
```

Esse script lê os arquivos CSV da pasta `data/` e carrega as tabelas no PostgreSQL.

### 6. Crie a view analítica

Execute o conteúdo do arquivo `Scripts/vw_vendas.sql` no PostgreSQL (via pgAdmin ou psql) para criar a view `public.vw_vendas_completa`.

### 7. Abra o dashboard

- Abra o arquivo `Dashboard/Dashboard_Vendas_Olist.pbix`
- Atualize as conexões do banco
- Verifique se o dashboard está apontando para o banco configurado

## Observações

- O script de ingestão assume que os arquivos CSV já estão presentes na pasta `data/`
- A estrutura do SQL pode ser ajustada conforme a necessidade de modelagem e KPIs do painel
- O projeto foi pensado como base para análise analítica e benchmarking de performance comercial

## Referências

- Olist Brazilian E-Commerce Dataset
- Kaggle

## Licença

Este projeto foi desenvolvido para fins acadêmicos e analíticos. Verifique a licença do dataset original antes de uso comercial ou distribuição externa.
