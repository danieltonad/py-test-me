import pytest
import sources.functions as func


def test_add():
    result = func.add(23, 89)
    assert result == 112
    
    
test_add()