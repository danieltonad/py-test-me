import pytest
from sources import functions as func


def test_add():
    result = func.add(3, 2)
    assert result == 5
    

def test_divide():
    with pytest.raises(ZeroDivisionError):
        func.divide(10, 0)
    assert True