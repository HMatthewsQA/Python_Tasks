import pytest
from Code import sum13

def test_sum13():
    assert sum13.sum13([13, 1, 2, 13, 2, 1, 13]) == 3