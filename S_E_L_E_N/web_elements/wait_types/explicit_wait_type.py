from traceback import print_stack
from klasa import PobieramElementy
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import *    


class ExplicitWaitType():
    
    def __init__(self, driver):
        self.driver = driver
        self.pe = PobieramElementy(driver)
        
    def waitForElement(self, locator, locatorType = 'id',timeout_1=10, pollFrequency_1=0.5):
        element = None
        try:
            byType = self.pe.getByType(locatorType)
            print(f'Waiting for maximum:: {timeout_1} :: second for element to be visible')
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=pollFrequency_1, ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotSelectableException]) 
            element = wait.until(EC.visibility_of_element_located((byType, locator))) # uwaga na ilośc nawiasów
            print('Element appeared on the web page')
        except:
            print('Element not appeared on the page')
            print_stack()  # ślad stosu
        return element                            
        
        
        
        
        
