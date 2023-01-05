import json
import requests


def api_scraper(url, file):
    res = requests.request("GET", url)
    json_data = res.json()
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
