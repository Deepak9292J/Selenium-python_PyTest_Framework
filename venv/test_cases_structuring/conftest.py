import pytest

@pytest.fixture()
def setUp():
    print("Prints before every method")
    yield
    print("Prints after every method")

@pytest.fixture(scope="module")
def OneTimeSetUp():
    print("One Time setup before any module")
    yield
    print("One Time setup after any module")