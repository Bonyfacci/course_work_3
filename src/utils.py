import json
import datetime


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
    return five_operations[-5:]


def date_processing(date):
    data = datetime.datetime.strptime(' '.join(date.split('T')), '%Y-%m-%d %H:%M:%S.%f')
    return data.date().strftime('%d.%m.%Y')


def information_output(list_operations):
    for i in list_operations:
        data = date_processing(i['date'])
        description = i['description']

        account = i['from'].split()[-1]
        check = account[0:4] + ' ' + account[4:6] + 2 * '*' + ' ' + 4 * '*' + ' ' + account[-5:-1]
        operation_from = ' '.join(i['from'].split()[0:-1]) + ' ' + check
        operation_to = i['to'].split()[0].strip() + ' **' + i['to'][-5:-1]

        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']

        print( f'{data} {description}\n' \
               f'{operation_from} -> {operation_to}\n' \
               f'{amount} {currency}\n')
