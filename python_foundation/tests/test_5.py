import pytest
import sys
sys.path.append('..')

from exercise5 import exercise5

@pytest.mark.parametrize("a, b, c, expected", [(1, 2, 3, 2), (8, 8, 10, 8), (1, 3, 6, 3)])
def test(a, b, c, expected):
    assert exercise5(a, b, c) == expected