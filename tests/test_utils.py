import pytest

from src import utils


def test_read_file():
    with pytest.raises(FileNotFoundError):
        utils.read_file("tests/data/test.txt") == "test"
