import pytest
from Code import scrambler

def test_scrambler():
	assert scrambler.scrambler('12345','abcde') == '1a2b3c4d5e'