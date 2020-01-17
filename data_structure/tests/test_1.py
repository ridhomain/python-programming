import pytest
import sys
sys.path.append('..')

from exercise1 import exercise1

@pytest.mark.parametrize("a, expected", [([3, 5], 8), ([], 0), ([1, 3, 4, 8, 10], 26)])
def test(a, expected):
    assert exercise1(a) == expected