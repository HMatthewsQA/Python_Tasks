import pytest
from Code import integral

def test_int():
    assert integral.createdict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}