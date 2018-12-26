import pytest

@pytest.mark.usefixtures("OneTimeSetUp" , "setUp")
class TestClassDemo():

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running test method B")
