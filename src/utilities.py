import os
from const import DATA_DIR, DATE
import datetime


def delete_json():
    '''
    Function that deletes json file which is no longer needed
    :return:
    '''
    os.remove(os.path.join(DATA_DIR, f'exchange_rate_PLN_{DATE}.json'))


def list_of_dates() -> list[str]:
    '''
    Function that creates list of dates from the chosen start date and creates as many dates as needed
    :return:
    '''
    start = datetime.date(2023, 1, 11)
    number_of_days_between_the_oldest_file_and_now = 31
    date_list = []

    for day in range(number_of_days_between_the_oldest_file_and_now):
        date = (start + datetime.timedelta(days=day)).isoformat()
        date_list.append(date)
    return date_list
