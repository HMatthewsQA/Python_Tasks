import pytest
from Code import classes

def test_classes():
    John = classes.Student("John", "21","A")
    assert John.avg_test(3,5,7) == 5