import pytest
import sys
sys.path.append('..')

from exercise2 import exercise2

@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (10, 5, 10)])
def test(a, b, expected):
    assert exercise2(a, b) == expected