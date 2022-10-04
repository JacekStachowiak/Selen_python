from selenium.webdriver.common.by import By

class SelenDriver():
    
    def __init__(self, driver):
        self.driver = driver
    
    def getByType(self, locatorType):        # def dla By.ID i By.Xpath
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css_selector':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'link_text':
            return By.LINK_TEXT
        else:
            print(f'Ten typ locatora {locatorType} nie jest wspierany/nie jest dobry')
        return False            

    def getElement(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator) 
            print('Element Found')           
        except:
            print('Element not found')
        return element            

# aby sprawdzić czy element jest obecny na stronie - czy będzie false czy True cały czas testujemy (nie wyrzuci)
    def isElementPresent(self, byType, locator):
        try:
            element = self.driver.find_element(byType, locator) # By.Id, 'name'
            if element is not None:
                print('Element Found')
                return True
            else: 
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False
    
    # drugi sposób na obecność elementu
    def isElementCheck(self, byType, locator):
        try:
            elementList = self.driver.find_elements(byType, locator) # By.Id, 'name'
            if len(elementList) > 0:
                print('Element Found')
                return True
            else:
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False