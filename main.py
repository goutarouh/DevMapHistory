from pandas import DataFrame

from processing import json_loader
from visualization import map_creator


def main():
    # json_loader.load_json_with_ijson("location_history.json")
    data: DataFrame = json_loader.load_csv()
    map_creator.map_creator(data)
    map_creator.plot_target_date_location_history(data)


if __name__ == '__main__':
    main()
