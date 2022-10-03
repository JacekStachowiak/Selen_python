from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTest(unittest.TestCase):
    
    def testLoginValid(self):
        
        baseURL = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login('test@email.com','abcabc')
       
        userIcon = driver.find_element(By.XPATH, '//div[@class="dropdown"]')
        if userIcon is not None:
            print('Login Successfull')
        else:
            print('Login Failed')
        
        driver.quit()
