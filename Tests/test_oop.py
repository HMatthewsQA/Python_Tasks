import pytest
from Code import oop

def test_oop():
    John = oop.Dodo()
    assert getattr(John, 'extinct') == True