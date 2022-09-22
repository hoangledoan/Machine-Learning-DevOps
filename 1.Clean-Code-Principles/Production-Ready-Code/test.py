import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")
    
@pytest.fixture
def innermost(order):
    order.append("innermost top")

def test_order(order, top):
    assert order == ["innermost top", "top"]

def test_order(order, innermost):
    assert order == ["innermost top"]

