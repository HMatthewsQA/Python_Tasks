import pytest
from Code import count_evens

def test_count_evens():
    assert count_evens.count_evens([1, 3, 5]) == 0