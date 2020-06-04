import pytest
from Code import double_char

def test_double_char():
    assert double_char.double_char('ABC') == 'AABBCC'