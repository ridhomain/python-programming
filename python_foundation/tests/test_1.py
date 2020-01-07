import pytest
import sys
sys.path.append('..')

from exercise1 import exercise1

@pytest.mark.parametrize("a, b, expected", [(3, 5, 8), (-1, 2, 1)])
def test(a, b, expected):
    assert exercise1(a, b) == expected