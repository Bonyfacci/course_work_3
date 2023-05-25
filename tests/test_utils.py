import pytest

from src import utils


def test_read_file():
    assert utils.read_file('for_test.json') == [{"word":"питон","subwords":["пони","тон"]},
  {"word":"набор","subwords":["бар","бон"]},
  {"word":"строка","subwords":["акр","акт"]}
]
    with pytest.raises(FileNotFoundError):
        utils.read_file("tests/data/test.txt")


@pytest.mark.parametrize('operations, expected', [
    ({}, []),
    ({'a': 1}, []),
    ({'a': 1, 'b': 2}, []),
    ({'a': 1, 'b': 2, 'c': 3}, []),
    ([{
    "id": 509552992,
    "state": "EXECUTED",
    "date": "2019-04-19T12:02:30.129240",
    "operationAmount": {
      "amount": "81513.74",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 9171987821259925",
    "to": "МИР 2052809263194182"
  },
], [{
    "id": 509552992,
    "state": "EXECUTED",
    "date": "2019-04-19T12:02:30.129240",
    "operationAmount": {
      "amount": "81513.74",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 9171987821259925",
    "to": "МИР 2052809263194182"
  },
])
])
def test_last_operations(operations, expected):
    assert utils.last_operations(operations) == expected
    with pytest.raises(TypeError):
        utils.last_operations() == []


def test_date_processing():
    assert utils.date_processing("2019-06-30T15:11:53.136004") == '30.06.2019'
    with pytest.raises(ValueError):
        utils.date_processing("test")


@pytest.mark.parametrize('operations, expected', [
    ([], None),
    ([{"date": "2019-06-30T15:11:53.136004",
    "operationAmount": {
      "amount": "95860.47",
      "currency": {
        "name": "руб."
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 59956820797131895975",
    "to": "Счет 43475624104328495820"
  }], None)
])
def test_information_output(operations, expected):
    assert utils.information_output(operations) == expected
    with pytest.raises(TypeError):
        utils.information_output("test")
        utils.information_output(([1, 2]))
        utils.information_output((['1', '2']))
