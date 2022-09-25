from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Element_state():
    
    def isEnabled(self):
        baseUrl = 'https://www.google.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)
        
        e1 = driver.find_element(By.NAME, 'q')
        e2 = driver.find_element(By.XPATH, '//div[@class="QS5gu sy4vM"]')
        e2.click()
        e1.send_keys('letskodeit')
        time.sleep(5)
        
    # może być że element id będzie disable a nie enable - wtedy trzeba poszukać id enable
        driver.quit()

run_test = Element_state()
run_test.isEnabled()   