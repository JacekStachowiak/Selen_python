from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixture('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
    
    @pytest.mark.run(order=2) 
    def test_ValidLogin(self):
        self.lp.login2('test@email.com','abcabc')
        result = self.lp.verifyLoginSuccessfull()
        assert result == True
            
    @pytest.mark.run(order=1)    
    def test_InvalidLogin(self):
        self.lp.login1('test@email.com123','abcabcASDFGH')
        result = self.lp.verifyLoginFailed()
        assert result == True
            
