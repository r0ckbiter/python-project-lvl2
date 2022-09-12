import os
import json
import yaml

JSON = ('.json',)
YAML = ('.yml', '.yaml')


def get_data(filepath):
    _, extension = os.path.splitext(filepath)
    file_extension = extension.lower()
    with open(filepath, 'r') as file_data:
        if file_extension in JSON:
            data = json.load(file_data)
        elif file_extension in YAML:
            data = yaml.safe_load(file_data)
    return data
