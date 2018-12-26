"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""


import pytest

@pytest.fixture()
def setUp_3():
    print("Prints before every method")
    yield
    print("Prints after every method")

def test_methodC(setUp_3):
    print("Running method C")

def test_methodD(setUp_3):
    print("Running test method D")

