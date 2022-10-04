from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):
    
    baseURL = 'https://courses.letskodeit.com/'
    #options=Options
    #options.add_argument("start-maximized")
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)
    
    @pytest.mark.run(order=2) 
    def test_ValidLogin(self):
        self.lp.login('test@email.com','abcabc')
        result = self.lp.verifyLoginSuccessfull()
        assert result == True
        self.driver.quit()
    
    @pytest.mark.run(order=1)    
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login('test@email.com','abcabcDSSAGDVB')
        result = self.lp.verifyLoginFailed()
        assert result == True
            
