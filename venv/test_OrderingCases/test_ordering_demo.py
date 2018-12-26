import pytest

@pytest.mark.run(order=3)
def test_methodB():
    print("Running test method B")

@pytest.mark.run(order=4)
def test_methodC():
    print("Running test method C")

@pytest.mark.run(order=1)
def test_methodD():
    print("Running test method D")

@pytest.mark.run(order=2)
def test_methodA():
    print("Running method A")
