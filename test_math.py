import pytest
from function import *


def test_add0():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.fixture
def some_data():
    return [1, 2, 3]


def test_data(some_data):
    assert len(some_data) == 3
    assert 2 in some_data


# def test_add():
#     x = 2
#     y = 3
#     result = add(x, y)
#     pytest.set_trace()
#     assert result == 5

def test_add_invalid_input():
    with pytest.raises(ValueError):
        add(None, 1)
    with pytest.raises(ValueError):
        add(1, None)
    with pytest.raises(ValueError):
        add(None, None)
