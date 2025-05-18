import json


def get_payload_json(file_path):
    payload_json = load_json_data_from_file(file_path)
    return payload_json

def load_json_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
