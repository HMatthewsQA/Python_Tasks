import pytest
from Code import passcheck

def test_passcheck():
	assert passcheck.passcheck(["ABd1234@1","a F1#","2w3E*","2We3345"]) == ["ABd1234@1"]