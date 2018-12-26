import pytest

@pytest.mark.run(order=3)
def test_methodB(oneTimeSetUp, setUp):
    print("Running test method B")

@pytest.mark.run(order=4)
def test_methodC(oneTimeSetUp, setUp):
    print("Running test method C")

@pytest.mark.run(order=1)
def test_methodD(oneTimeSetUp, setUp):
    print("Running test method D")

@pytest.mark.run(order=2)
def test_methodA(oneTimeSetUp, setUp):
    print("Running method A")
