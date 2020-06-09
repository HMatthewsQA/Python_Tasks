import pytest
from Code import commasep

def test_commasep():
    assert commasep.commasep('without,hello,bag,world') == ['bag', 'hello', 'without', 'world']