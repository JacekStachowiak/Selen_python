from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import *
import utilities.custom_logger as cl  
import logging
import time
import os


class SelenDriver():
    
    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        self.driver = driver
    
    def screenShot(self, resultMessage):
        fileName = resultMessage + '.' + str(round(time.time()*1000)) + '.png'
        screenshotDirectory = '../screenshots/'
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f'Screenshot save to directory: {destinationFile}')                
        except:
            self.log.error('### Exception occurred ###')            
            print_stack()
        
    
    def getTitle(self):
        return self.driver.title        
    
    def getByType(self, locatorType):        # def dla By.ID i By.Xpath
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            self.log.info(f'Ten typ locatora {locatorType} nie jest wspierany/nie jest dobry')
        return False            

    def getElement(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator) 
            self.log.info(f'Element Found with locator: {locator} and locatorType: {locatorType}')           
        except:
            self.log.info(f'Element not found with locator: {locator} and locatorType: {locatorType}')
        return element      
    
    # nowa metoda
    def getElementList(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator) 
            self.log.info(f'Element Found with locator: {locator} and locatorType: {locatorType}')           
        except:
            self.log.info(f'Element not found with locator: {locator} and locatorType: {locatorType}')
        return element  
    
    
    def elementClick(self, locator='', locatorType='id', element=None):
        # zmodyfikowany o if
        try:
            if locator: # is True
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Click on element with locator: {locator}, locatorType: {locatorType}')
        except:
            self.log.info(f'Cannot click on element with locator: {locator}, locatorType: {locatorType}')
            print_stack()            

    
    def sendKeys(self, data, locator='', locatorType='id', element=None):
        # zmodyfikowany
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'Send data on element with locator: {locator}, locatorType: {locatorType}')
        except:
            self.log.info(f'Send data on element with locator: {locator}, locatorType: {locatorType}')
            print_stack() 
    
    # nowa metoda
    def getText(self, locator='', locataorType='id', element=None, info=''):
        
        try:
            if locator:
                self.log.debug('In locator condytion')
                element = self.getElement(locator, locataorType)
            self.log.debug('Before finding text')
            text = element.text
            self.log.debug(f'After finding element, size is: {str(len(text))}') 
            if len(text) == 0:
                text = element.get_attribute('inner text')
            if len(text) != 0:
                self.log.info(f'Getting text on element: {info}')
                self.log.info(f'The text is:: "{text}"')
                text = text.strip()
        except:
            self.log.error(f'Failed to get text on element: {info}')
            print_stack()
            text = None
        return text
  
    # aby sprawdzić czy element jest obecny na stronie - czy będzie false czy True cały czas testujemy (nie wyrzuci)
    def isElementPresent(self, locator='', locatorType='id', element=None):
        # zmodyfikowany
        try:
            if locator:
                element = self.getElement(locator, locatorType) # By.Id, 'name'
            if element is not None:
                self.log.info(f'Element present with locator: {locator}, locatorType: {locatorType}')
                return True
            else: 
                self.log.info(f'Element not present with locator: {locator}, locatorType: {locatorType}')
                return False
        except:
            self.log.info('Element not found')
            return False
    
    
    # nowa metoda
    def isElementDisplayed(self, locator='', locatorType='id', element = None):
        
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:                
                isDisplayed = element.is_displayed()
                self.log.info(f'Element is displayed with locator: {locator}, locatorType: {locatorType}') 
            else:
                self.log.info(f'Element is not displayed with locator: {locator}, locatorType: {locatorType}')                
            return isDisplayed
        except:
            print('Element not found')
            return False
    
    
    # drugi sposób na obecność elementu
    def elementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator) # By.Id, 'name'
            if len(elementList) > 0:
                self.log.info(f'Element present with locator: {locator}, locatorType: {byType}')
                return True
            else:
                self.log.info(f'Element not present with locator: {locator}, locatorType: {byType}')
                return False
        except:
            self.log.info('Element not found')
            return False
    
    
    def waitForElement(self, locator, locatorType='id',timeout_1=10, pollFrequency_1=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info(f'Waiting for maximum:: {timeout_1} :: second for element to be visible')
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=pollFrequency_1, ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotSelectableException]) 
            element = wait.until(EC.visibility_of_element_located((byType, locator))) # uwaga na ilośc nawiasów
            self.log.info('Element appeared on the web page')
        except:
            self.log.info('Element not appeared on the page')
            print_stack()  # ślad stosu
        return element   
    
    
    def webScroll(self, direction='up'):
        # new method
        if direction == 'up':
            self.driver.execute_script('window.scrollBy(0, -1000);')

        if direction == 'down':
            self.driver.execute_script('window.scrollBy(0, 1000);')