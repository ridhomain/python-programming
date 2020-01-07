import pytest
import sys
sys.path.append('..')

from exercise10 import exercise10

@pytest.mark.parametrize("a, expected", [('abcdef', 'ace'), ('python', 'pto')])
def test(a, expected):
    assert exercise10(a) == expected