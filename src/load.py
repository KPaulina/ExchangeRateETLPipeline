import json
from utilities import list_of_dates
from pymongo import MongoClient
import psycopg2
from sqlalchemy.exc import OperationalError
from transformation import json_to_dataframe
from sqlalchemy import create_engine
from const import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATE, DATA_DIR, MANGODB_CONNECTION
import os
''''
Load data to the following table
    CREATE TABLE exchange_rate_PLN (
    id serial PRIMARY KEY not null,
    currency_code varchar(10),
	provider varchar(50),
    time_last_update_utc varchar(50),
    rates numeric,
    updated_at date)
'''''

#mongodb connection
client = MongoClient(MANGODB_CONNECTION)
db = client.exchange_rate
collection = db.PLN_json


def load_data_to_postgres():
    '''
    Function that loads chosen from json data to postgres
    :return:
    '''
    df_exchange_rate = json_to_dataframe()
    try:
        db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        df_exchange_rate.to_sql('exchange_rate_pln', db, schema='public', if_exists='append', index=False)
    except psycopg2.Error as error:
        print(f'Error: {error}')
    except OperationalError as error:
        print(f'Operational error: {error}')


def load_json_to_mongodb():
    '''
    Function that takes the whole json data into MongoDB
    :return:
    '''
    with open(os.path.join(DATA_DIR, f'exchange_rate_PLN_{DATE}.json'), 'r') as file:
        data = json.load(file)
    collection.insert_one(data)


def bulk_load_of_old_json_files():
    '''
    Function that helps to load older data in json to MongoDB
    :return:
    '''
    #list of dates that is needed in order to insert data into MongoDB
    dates = list_of_dates()
    for date in dates:
        try:
            with open(os.path.join(DATA_DIR, f'exchange_rate_PLN_{date}.json'), 'r') as file:
                data = json.load(file)
                collection.insert_one(data)
        except FileNotFoundError as error:
            print(error)


