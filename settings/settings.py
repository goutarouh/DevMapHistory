import configparser
from datetime import datetime

ini_file = configparser.SafeConfigParser()
ini_file.read('settings.ini')


def is_load_json() -> bool:
    return ini_file.getboolean('DEFAULT', "load_json")


def start_date_str() -> str:
    return ini_file.get('DEFAULT', 'start_date')


def start_date() -> datetime:
    return datetime.strptime(start_date_str(), '%Y-%m-%d %H:%M:%S')


def end_date_str() -> str:
    return ini_file.get('DEFAULT', 'end_date')


def end_date() -> datetime:
    return datetime.strptime(end_date_str(), '%Y-%m-%d %H:%M:%S')


def data_csv_path() -> str:
    return ini_file.get('DEFAULT', 'data_csv_path')


def processed_data_csv_path() -> str:
    return ini_file.get('DEFAULT', 'processed_data_csv_path')


def location_history_json() -> str:
    return ini_file.get('MY_SETTINGS', 'location_history_path')
