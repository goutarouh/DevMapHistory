from pandas import DataFrame

from processing import json_loader
from visualization import map_creator
from settings import settings


def main():
    if settings.is_load_json():
        json_loader.load_json_with_ijson(settings.location_history_json())
    data: DataFrame = json_loader.load_csv()
    map_creator.map_creator(data)
    map_creator.plot_target_date_location_history(data)


if __name__ == '__main__':
    main()
