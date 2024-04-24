import logging
import json

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """
    Reading json file and return dict
    :param path: str - path to json file:
    :return dict of data from json file:
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            paths = json.load(file)
        return paths
    except Exception as e:
        logging.error(f"Error in json_reader - {e}")
