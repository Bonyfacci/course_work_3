import json


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


def last_operations(operations):
    five_operations = []
    for i in operations:
        if 'date' in i and 'state' in i and 'from' in i and i['state'] == 'EXECUTED':
            five_operations.append(i)
    five_operations = sorted(five_operations, key=lambda d: d['date'])
    return five_operations[-6:-1]
