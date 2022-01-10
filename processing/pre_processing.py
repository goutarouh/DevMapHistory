import pandas as pd
import numpy as np

from processing import json_loader
from util import date_formatter
from settings import settings


def pre_process():
    start_time_stamp_ms = int(settings.start_date().timestamp() * 10 ** 3)
    end_time_stamp_ms = int(settings.end_date().timestamp() * 10 ** 3)
    t_new = np.arange(start_time_stamp_ms, end_time_stamp_ms, 1000 * 30).astype('float64')
    t_new_datetime = [date_formatter.unix_time_to_datetime(t // 10**3) for t in t_new]

    data = json_loader.load_csv(settings.data_csv_path())
    data_ndarray = data.values
    t_data = data_ndarray[:, 1].astype('float64')
    lat_data = data_ndarray[:, 3].astype('float64')
    long_data = data_ndarray[:, 4].astype('float64')

    interp_latitude = np.interp(t_new, t_data, lat_data)
    interp_longitude = np.interp(t_new, t_data, long_data)

    df = pd.DataFrame(
        data={
            'time_stamp_ms': t_new,
            'datetime': t_new_datetime,
            'latitude': interp_latitude,
            'longitude': interp_longitude
        }
    )

    df.to_csv("output/processed_data.csv")