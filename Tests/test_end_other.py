import pytest
from Code import end_other

def test_end_other():
    assert end_other.end_other('abc', 'abXabc') == True