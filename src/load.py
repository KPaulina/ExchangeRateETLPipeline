import os
from transformation import json_to_dataframe
from sqlalchemy import create_engine
from const import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
''''
Load data to the following table
    CREATE TABLE exchange_rate_PLN (
    id serial PRIMARY KEY not null,
    currency_code varchar(10),
    time_last_update_utc varchar(50),
    rates numeric,
    updated_at varchar(6) default to_char(CURRENT_DATE, 'yyyymm')
'''''


def load_data():
    df_exchange_rate = json_to_dataframe()

    db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    conn = db.connect()

    df_exchange_rate.to_sql('exchange_rate_pln', conn, schema='public', if_exists='append', index=False)
