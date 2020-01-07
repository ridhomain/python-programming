import pytest
import sys
sys.path.append('..')

from exercise4 import exercise4

@pytest.mark.parametrize("a, expected", [(2, True), (5, False)])
def test(a, expected):
    assert exercise4(a) == expected