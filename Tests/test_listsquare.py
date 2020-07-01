import pytest
from Code import listsquare

def test_listsquare():
	assert listsquare.listsquare([2,4,6,8,9]) == [81]
	assert listsquare.listsquare([1,3]) == [1,9]