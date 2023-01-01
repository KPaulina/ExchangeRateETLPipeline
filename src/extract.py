import json
import requests
from datetime import datetime

time = str(datetime.now())[:10]


def json_scraper(url, file):
    res = requests.request("GET", url)
    json_data = res.json()

    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


json_scraper('https://open.er-api.com/v6/latest/PLN', f"exchange_rate_PLN_{time}.json")
