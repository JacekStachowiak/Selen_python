# wdf = WebDriverFactory(browser)
# wdf.getWebDriverInstance()

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class WebDriverFactory():
    
    def __init__(self, browser):
        self.browser = browser
    
    def getWebDriverInstance(self):
        
        baseURL = 'https://courses.letskodeit.com/login'
        if self.browser == 'iexplorer':
            driver = webdriver.Ie()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                    
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver    
