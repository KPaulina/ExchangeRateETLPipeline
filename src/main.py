from extract import api_scraper
from const import DATA_DIR, DATE
from load import load_data_to_postgres, load_json_to_mongodb, bulk_load_of_old_json_files
from utilities import delete_json
import os

if __name__ == "__main__":
    api_scraper('https://open.er-api.com/v6/latest/PLN', os.path.join(DATA_DIR, f'exchange_rate_PLN_{DATE}.json'))
    load_data_to_postgres()
    load_json_to_mongodb()
    delete_json()
    # bulk_load_of_old_json_files()

