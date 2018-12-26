"""
In order to pass the environment related arguments in the command line, we need to use the
below command-

py.test -s -v module_name.py --browser browser_name

"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
    yield
    print("Running one time tearDown")

# pytest_addoption(parser) -- It is a special method which is related to pytest. The method name should not be changed here.
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")