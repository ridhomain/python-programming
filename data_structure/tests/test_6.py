import pytest
import sys
sys.path.append('..')

from exercise6 import exercise6

@pytest.mark.parametrize("a, expected", [({"a": 1, "b": 3}, 3), ({"a": 2, "b": 4, "c": 10, "d": 6}, 10)])
def test(a, expected):
    assert exercise6(a) == expected