from selenium.webdriver.common.by import By
from base.selen_driver import SelenDriver
import utilities.custom_logger as cl  
import logging
class LoginPage(SelenDriver):
    
    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # locators
    _login_link = '//a[text()="Sign In"]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _all_Course = '//a[text()="ALL COURSES"]'
    
    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)
    
    # def getAllCourse(self):
    #     return self.driver.find_element(By.XPATH, self._all_Course)
        
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='xpath')
    
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='id')
    
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType='id') 
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')
    
    def clickAllCourse(self):
        self.elementClick(self._all_Course, locatorType='xpath')


    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.clickAllCourse()
