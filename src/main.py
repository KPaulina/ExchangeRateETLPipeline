from extract import json_scraper
from datetime import datetime
from load import load_data

time = str(datetime.now())[:10]

if __name__ == "__main__":
    json_scraper('https://open.er-api.com/v6/latest/PLN', f"exchange_rate_PLN_{time}.json")
    load_data()
