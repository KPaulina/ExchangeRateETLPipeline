import os
from transformation import json_to_dataframe
from sqlalchemy import create_engine
import dotenv
''''
Load data to the following table
    CREATE TABLE exchange_rate_PLN (
    id serial PRIMARY KEY not null,
    currency_code varchar(10),
    time_last_update_utc varchar(50),
    rates numeric,
    updated_at varchar(6) default to_char(CURRENT_DATE, 'yyyymm')
'''''
dotenv.load_dotenv()

DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')

df_exchange_rate = json_to_dataframe()

db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
conn = db.connect()

df_exchange_rate.to_sql('exchange_rate_pln', conn, schema='public', if_exists='append', index=False)
