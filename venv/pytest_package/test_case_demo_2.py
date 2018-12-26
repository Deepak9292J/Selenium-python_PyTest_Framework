import pytest

@pytest.fixture()
def setUp_2():
    print("Prints before every method")

def test_methodC(setUp_2):
    print("Running method C")

def test_methodD(setUp_2):
    print("Running test method D")

