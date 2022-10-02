import pytest


@pytest.fixture()
def setUp():
    print('Uruchamiam method level setUp')
    yield
    print('Uruchamiam method level tearDown')


@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print('Uruchamiam one time setUp')
    if browser == 'firefox':
        value = 10
        print('Running tests on FF')
    else:
        value = 20
        print('Running tests on Chrome')

    if request.cls is not None:
        request.cls.value = value

    yield value
    print('Uruchamiam one time tearDown')


def pytest_addoption(parser):
    parser.addoption("--browser")   # rodzaj przeglądarki
    # rodzaj systemu(Mac, Win)
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")
