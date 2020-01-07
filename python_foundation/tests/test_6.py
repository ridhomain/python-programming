import pytest
import sys
sys.path.append('..')

from exercise6 import exercise6

@pytest.mark.parametrize("a, expected", [(2000, True), (1996, True), (1800, False), (2013, False)])
def test(a, expected):
    assert exercise6(a) == expected