import ijson
import pandas as pd
from pandas import DataFrame

from settings import settings
from util import date_formatter
from datetime import datetime


def load_json_with_ijson(file_path: str):
    df = pd.DataFrame(columns=["time_stamp_ms", "datetime", "latitude", "longitude"])
    with open(file_path, 'r') as json_file:
        ijson_generator = ijson.items(json_file, "locations.item")
        for index, location in enumerate(ijson_generator):
            time_stamp_ms = int(location['timestampMs'])
            history_datetime = date_formatter.unix_time_to_datetime(time_stamp_ms // 10 ** 3)
            str_history_datetime = date_formatter.datetime_to_str(history_datetime)
            latitude = int(location['latitudeE7']) / 10 ** 7
            longitude = int(location['longitudeE7']) / 10 ** 7
            if filter_date(history_datetime):
                df.loc[index] = [time_stamp_ms, str_history_datetime, latitude, longitude]

    df.to_csv(settings.output_csv_path())


def filter_date(history_datetime: datetime) -> bool:
    start = datetime.strptime(settings.start_date(), '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(settings.end_date(), '%Y-%m-%d %H:%M:%S')
    is_in_target_range = start < history_datetime < end
    return is_in_target_range


def load_csv() -> DataFrame:
    return pd.read_csv(settings.output_csv_path())
