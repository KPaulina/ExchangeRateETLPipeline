import json
import requests


def json_scraper(url, file):
    res = requests.request("GET", url)
    json_data = res.json()

    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)



