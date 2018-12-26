import pytest

@pytest.fixture()
def setUp():
    print("Prints before every method")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running test method B")

