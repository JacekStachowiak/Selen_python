from unittest import result
from selenium.webdriver.common.by import By
from base.selen_driver import SelenDriver
import utilities.custom_logger as cl  
import logging
import time
class LoginPage(SelenDriver):
    
    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # locators
    _login_link = '//a[text()="Login"]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _all_Course = '//a[text()="ALL COURSES"]'
    
    
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='link')
    
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='id')
    
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType='id') 
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')
    
    def clickAllCourse(self):
        self.elementClick(self._all_Course, locatorType='xpath')

    def login1(self, email='', password=''):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()
        # self.clickAllCourse()
    
    def login2(self, email='', password=''):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()
        self.clickAllCourse()
    
    def verifyLoginSuccessfull(self):
        result = self.isElementPresent('//*[@id="navbar-inverse-collapse"]/div[1]/div', locatorType='xpath')
        return result
    
    def verifyLoginFailed(self):
        result = self.isElementPresent('//span[text()="Your username or password is invalid. Please try again."]', locatorType='xpath')
        return result
    
    def verifyTitle(self):
        if "All Courses" in self.getTitle():    # "All Courses"
            return True
        else:
            return False
    
    def clearFields(self):
        emailFields = self.getElement(locator=self._email_field)    
        emailFields.clear()
        passwordFields = self.getElement(locator=self._password_field)
        passwordFields.clear()        
