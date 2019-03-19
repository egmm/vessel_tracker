import json
import csv

SHIPS_PATH = "./ships.json"
POSITION_PATH = "./position.json"
CSV_SOURCE_PATH = "./positions.csv"
SHIPS = {
    "9632179": "Mathilde Maersk",
    "9247455": "Australian Spirit",
    "9595321": "MSC Preziosa"
}


def parse_db_record(data, key):
    imo, timestamp, latitude, longitude = data
    return {
        "model": "tracking.Position",
        "pk": key,
        "fields": {
            "imo": [imo],
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude

        }
    }


def add_data_to_file(data, filepath):
    with open(filepath, 'w') as fixtures:
        json.dump(data, fixtures)


def position_table(filepath, output_path):
    # Read the csv file and construct the initial_data.json file
    with open(filepath) as positions_file:
        data = []
        positions = csv.reader(positions_file)
        for key, position in enumerate(positions):
            new_record = parse_db_record(position, key + 1)
            data.append(new_record)

        add_data_to_file(data, output_path)


def ship_table():
    ships = []
    for key, ship in enumerate(SHIPS):
        ships.append({
            "model": "tracking.Ship",
            "pk": key + 1,
            "fields": {
                "imo": ship,
                "name": SHIPS[ship]
            }
        })
    add_data_to_file(ships, SHIPS_PATH)

ship_table()
position_table(CSV_SOURCE_PATH, POSITION_PATH)
