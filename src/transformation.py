import pandas as pd
from const import DATA_DIR, DATE
import os


def json_to_dataframe():
    df_exchange_rate = pd.read_json(os.path.join(DATA_DIR, f"exchange_rate_PLN_{DATE}.json"))
    df_exchange_rate.reset_index(inplace=True)
    df_exchange_rate = df_exchange_rate.rename(columns={'index': 'currency_code'})
    return df_exchange_rate[['currency_code', 'provider', 'time_last_update_utc', 'rates']]

