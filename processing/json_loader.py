import ijson

from util import date_formatter
from datetime import datetime


start = datetime.strptime('2021-12-29 00:00:00', '%Y-%m-%d %H:%M:%S')
end = datetime.strptime('2022-01-02 23:59:59', '%Y-%m-%d %H:%M:%S')


def load_json_with_ijson(file_path: str):
    with open(file_path, 'r') as json_file:
        ijson_generator = ijson.items(json_file, "locations.item")
        for location in ijson_generator:
            time_stamp = int(location['timestampMs']) // 1000
            if filter_date(time_stamp):
                converted_date: datetime = date_formatter.unix_time_to_date(time_stamp)
                print(converted_date)


def filter_date(time_stamp: int) -> bool:
    history_datetime = date_formatter.unix_time_to_date(time_stamp)
    is_in_target_range = start < history_datetime < end
    return is_in_target_range






