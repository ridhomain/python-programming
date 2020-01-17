import pytest
import sys
sys.path.append('..')

from exercise4 import exercise4

@pytest.mark.parametrize("a, b, expected", [(2, [1, 2, 3, 4], 1), (2, [], 0), (1, [1, 1, 1, 2, 3, 4], 3)])
def test(a, b, expected):
    assert exercise4(a, b) == expected