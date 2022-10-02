from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class LoginTest():
    
    def testLoginValid(self):
        
        baseURL = 'https://courses.letskodeit.com//'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.XPATH, '//a[text()="Sign In"]')
        loginLink.click()
        time.sleep(3)
        
        emailField = driver.find_element(By.ID, 'email')
        emailField.send_keys('test@email.com')
        
        passwordField = driver.find_element(By.ID, 'password')
        passwordField.send_keys('abcabc')
        
        loginButton = driver.find_element(By.XPATH, '//input[@class="btn btn-default btn-block btn-md dynamic-button"]')
        loginButton.click()
        time.sleep(5)
        allCourse = driver.find_element(By.XPATH, '//a[text()="ALL COURSES"]')
        allCourse.click()
        time.sleep(3)
        
        driver.quit()
        
run_test = LoginTest()
run_test.testLoginValid()         