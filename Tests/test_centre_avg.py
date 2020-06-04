import pytest
from Code import centre_avg

def test_centre_avg():
    assert centre_avg.centered_average([1, 1, 5, 5, 10, 8, 7]) == 5.2