import pandas as pd
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')

date = str(datetime.now())[:10]


def json_to_dataframe():
    df_exchange_rate = pd.read_json(os.path.join(DATA_DIR, f"exchange_rate_PLN_{date}.json"))
    df_exchange_rate.reset_index(inplace=True)
    df_exchange_rate = df_exchange_rate.rename(columns={'index': 'currency_code'})
    return df_exchange_rate[['currency_code', 'provider', 'time_last_update_utc', 'rates']]

