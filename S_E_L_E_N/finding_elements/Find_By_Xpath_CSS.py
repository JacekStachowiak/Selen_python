from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FindByXpathCSS():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        elementByXpath = driver.find_element(By.XPATH, '//input[@id="displayed-text"]')
        #sprawdzamy czy element jest
        if elementByXpath is not None:
            print('Element znaleziono --> By.Xpath')

        elementByCSS = driver.find_element(By.CSS_SELECTOR, '#displayed-text')
        if elementByCSS is not None:
            print('Element znaleziono --> By.CSS_SELECTOR')
        
        driver.close()

run_test = FindByXpathCSS()
run_test.test()