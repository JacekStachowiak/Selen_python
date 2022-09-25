from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from klasa import PobieramElementy
import time

# wykorzystujemy klasę i metody z pliku klasa.py

class ElementPresentCheck():
    
    def test(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        pe = PobieramElementy(driver)
        driver.get(baseUrl)

        elementResult_1 = pe.isElementPresent('id','name')        
        print(elementResult_1)
        
        elementResult_2 = pe.isElementCheck('xpath', '//input[@id="name"]')
        print(elementResult_2)
        
        driver.quit()

run_test = ElementPresentCheck()
run_test.test()        