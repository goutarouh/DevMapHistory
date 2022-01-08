import configparser

ini_file = configparser.SafeConfigParser()
ini_file.read('settings.ini')


def is_load_json() -> bool:
    return ini_file.getboolean('DEFAULT', "load_json")


def start_date() -> str:
    return ini_file.get('DEFAULT', 'start_date')


def end_date() -> str:
    return ini_file.get('DEFAULT', 'end_date')


def output_csv_path() -> str:
    return ini_file.get('DEFAULT', 'output_csv_path')


def location_history_json() -> str:
    return ini_file.get('MY_SETTINGS', 'location_history_path')
