from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_login():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        loginLink = driver.find_element(By.XPATH, '//div[@id="navbar-inverse-collapse"]//a[@href="/login"]')
        loginLink.click()
        
        emailField = driver.find_element(By.ID, 'email')
        emailField.send_keys('test')
        
        passwordField = driver.find_element(By.ID, 'password')
        passwordField.send_keys('test')
        
        emailField.clear()
        emailField.send_keys('test')
        #passwordField.clear()
        
        driver.quit()

run_test = Test_login()
run_test.test()        