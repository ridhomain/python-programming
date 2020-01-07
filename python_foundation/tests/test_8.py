import pytest
import sys
sys.path.append('..')

from exercise8 import exercise8

@pytest.mark.parametrize("a, expected", [(3, True), (41, True), (4, False), (50, False)])
def test(a, expected):
    assert exercise8(a) == expected