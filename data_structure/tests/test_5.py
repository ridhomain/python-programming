import pytest
import sys
sys.path.append('..')

from exercise5 import exercise5

@pytest.mark.parametrize("a, expected", [([1, 2, 3, 4], [0, 2, 0, 4]), ([1, 2, 3, 5, 5], [0, 2, 0, 0, 0]), ([4, 5, 6, 7, 8, 9, 10], [4, 0, 6, 0, 8, 0, 10])])
def test(a, expected):
    assert exercise5(a) == expected