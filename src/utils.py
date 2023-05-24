import json


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations
