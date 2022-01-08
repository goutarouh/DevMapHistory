import datetime
from datetime import datetime


def unix_time_to_date(unix_time: int) -> datetime:
    converted_datetime: datetime = datetime.fromtimestamp(unix_time)
    return converted_datetime
