import pytest
from Code import zipstring

def test_zipstring():
    assert zipstring.zipstring("Dog","Cat") == "DCoagt"