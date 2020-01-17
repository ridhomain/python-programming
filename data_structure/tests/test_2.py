import pytest
import sys
sys.path.append('..')

from exercise2 import exercise2

@pytest.mark.parametrize("a, expected", [([3, 5], 5), ([1, 3, 4, 8, 10], 10)])
def test(a, expected):
    assert exercise2(a) == expected