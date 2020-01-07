import pytest
import sys
sys.path.append('..')

from exercise9 import exercise9

@pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (14, 24, 2), (25, 30, 5), (1, 2, 1)])
def test(a, b, expected):
    assert exercise9(a, b) == expected