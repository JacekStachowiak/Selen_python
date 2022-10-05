import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print('Uruchamiam method level setUp')
    yield
    print('Uruchamiam method level tearDown')

@pytest.yield_fixture(scope='class')
def oneTimeSetUp(request, browser):
    print('Uruchamiam one time setUp')
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
   
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
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



#from selenium.webdriver.chrome.options import Options

 # if browser == 'firefox':
    #     driver = webdriver.Firefox()
    #     baseURL = 'https://courses.letskodeit.com/login'
    #     driver.get(baseURL)
    #     print('Running tests on FF')
    # else:
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     baseURL = 'https://courses.letskodeit.com/login'
    #     #options=Options
    #     #options.add_argument("start-maximized")
    #     #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print('Running tests on Chrome')   