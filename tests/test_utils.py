import pytest

from src import utils


def test_read_file():
    with pytest.raises(FileNotFoundError):
        utils.read_file("tests/data/test.txt") == "test"


@pytest.mark.parametrize('operations, expected', [
    ({}, []),
    ({'a': 1}, []),
    ({'a': 1, 'b': 2}, []),
    ({'a': 1, 'b': 2, 'c': 3}, [])
])
def test_last_operations(operations, expected):
    assert utils.last_operations(operations) == expected
    with pytest.raises(TypeError):
        utils.last_operations() == []
