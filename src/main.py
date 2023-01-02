from extract import json_scraper
from datetime import datetime
from load import load_data
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')

time = str(datetime.now())[:10]

if __name__ == "__main__":
    json_scraper('https://open.er-api.com/v6/latest/PLN', os.path.join(DATA_DIR, f'exchange_rate_PLN_{time}.json'))
    load_data()
