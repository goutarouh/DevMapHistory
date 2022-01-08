from processing import json_loader


def main():
    json_loader.load_json_with_ijson("location_history.json")


if __name__ == '__main__':
    main()
