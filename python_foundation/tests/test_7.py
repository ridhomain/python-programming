import pytest
import sys
sys.path.append('..')

from exercise7 import exercise7

@pytest.mark.parametrize("a, expected", [(2, 0), (333, 160)])
def test(a, expected):
    assert exercise7(a) == expected