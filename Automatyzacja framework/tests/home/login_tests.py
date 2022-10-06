from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixture('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    
    @pytest.mark.run(order=2) 
    def test_ValidLogin(self):
        self.lp.login2('test@email.com','abcabc')
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, 'Title verify')
        result2 = self.lp.verifyLoginSuccessfull()
        self.ts.markFinal('test_ValidLogin', result2, 'Login was successful')
       
            
    @pytest.mark.run(order=1)    
    def test_InvalidLogin(self):
        self.lp.login1('test@email.com123','abcabcASDFGH')
        result = self.lp.verifyLoginFailed()
        assert result == True
            
