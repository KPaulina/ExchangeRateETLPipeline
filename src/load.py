import json

from pymongo import MongoClient
import psycopg2
from sqlalchemy.exc import OperationalError
from transformation import json_to_dataframe
from sqlalchemy import create_engine
from const import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATE, DATA_DIR
import os
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
    try:
        db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        conn = db.connect()
        df_exchange_rate.to_sql('exchange_rate_pln', conn, schema='public', if_exists='append', index=False)
    except psycopg2.Error as error:
        print(f'Error: {error}')
    except OperationalError as error:
        print(f'Operational error: {error}')


def load_json_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.exchange_rate
    collection = db.PLN_json
    with open(os.path.join(DATA_DIR, f'exchange_rate_PLN_{DATE}.json'), 'r') as file:
        data = json.load(file)
    collection.insert_one(data)
