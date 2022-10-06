from base.selen_driver import SelenDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SelenDriver):
    
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util
    
    def verifyPageTitle(self, titleToVerify):
        
        try:
            actualTitle = self.getTitle()
            #return self.util.verifyTextMatch(actualTitle, titleToVerify)
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error('Failed to get page title')
            print_stack()
            return False
        
                