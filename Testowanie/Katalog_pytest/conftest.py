import pytest

@pytest.fixture()
def setUp():
    print('Uruchamiam method level setUp')
    yield
    print('Uruchamiam method level tearDown')
    
@pytest.fixture(scope='class')
def oneTimeSetUp(browser, osType):
    print('Uruchamiam one time setUp')
    if browser == 'firefox':
        print('Running tests on FF')
    else:
        print('Running tests on Chrome')        
    yield
    print('Uruchamiam one time tearDown') 

def pytest_addoption(parser):
    parser.addoption("--browser")   # rodzaj przeglądarki
    parser.addoption("--osType", help="Type of operating system")   # rodzaj systemu(Mac, Win)

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")        