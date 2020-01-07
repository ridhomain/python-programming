import pytest
import sys
sys.path.append('..')

from exercise3 import exercise3

@pytest.mark.parametrize("a, b, c, expected", [(3, 4 ,5 ,5), (-5, 3, 4 , 4)])
def test(a, b, c, expected):
    assert exercise3(a, b, c) == expected