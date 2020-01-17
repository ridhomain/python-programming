import pytest
import sys
sys.path.append('..')

from exercise3 import exercise3

a = [1, 2, 3]
b = [3]
c = []

@pytest.mark.parametrize("a, expected", [(a, a), (b, b), (c, c)])
def test(a, expected):
    assert exercise3(a) is not expected