import pytest

from src import utils


# @pytest.mark.parametrize("test_input, expected", [
#         ("tests/data/test.txt", "test")
# ])
def test_read_file():
    with pytest.raises(FileNotFoundError):
        utils.read_file("tests/data/test.txt") == "test"
