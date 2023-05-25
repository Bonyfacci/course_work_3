import json


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


def last_operations(operations):
    five_operations = []
    for i in operations:
        if 'date' in i and 'state' in i and 'from' != None and i['state'] == 'EXECUTED':
            five_operations.append(i['date'])
    five_operations.sort()
    return five_operations[-6:-1]
