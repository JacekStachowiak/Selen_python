import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CalendarSelection():
    
    def test1(self):
        
        baseUrl = 'https://www.expedia.com'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        driver.find_element(By.XPATH, '//span[text()="Flights"]').click()
        departingField = driver.find_element(By.XPATH, '//*[@id="d1-btn"]')
        departingField.click()
        dateToSelect = driver.find_element(By.XPATH, '//div[@class="uitk-date-picker-month"]//button[@data-day="31"]')                
        dateToSelect.click()

        time.sleep(2)
        driver.quit()
        
    def test2(self):
        baseUrl = 'https://www.expedia.com'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)    
        
        driver.find_element(By.XPATH, '//span[text()="Flights"]').click()
        departingField = driver.find_element(By.XPATH, '//*[@id="d1-btn"]')
        departingField.click()
        dateToSelect = driver.find_element(By.XPATH, '//div[@class="uitk-date-picker-month"]//button[@data-day="31"]')                
        dateToSelect.click()
        calMonth = driver.find_element(By.XPATH, '')
        
        time.sleep(2)
        driver.quit()

run_test = CalendarSelection()
run_test.test1()                
        