import datetime
from datetime import datetime


def unix_time_to_datetime(unix_time: int) -> datetime:
    converted_datetime: datetime = datetime.fromtimestamp(unix_time)
    return converted_datetime


def str_to_datetime(str_date: str) -> datetime:
    return datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')


def datetime_to_str(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')