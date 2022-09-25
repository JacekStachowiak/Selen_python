from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from klasa import PobieramElementy
import time

# wykorzystujemy klasę i metody z pliku klasa.py

class UsingWrapers():
    
    def test(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        pe = PobieramElementy(driver)
        driver.get(baseUrl)
        
        textField_1 = pe.getElement('name', 'id')
        textField_1.send_keys('Test')
        time.sleep(2)

        textField_2 = pe.getElement('//input[@id="name"]', 'xpath')
        textField_2.clear()
        textField_2.send_keys('Test_2')
        time.sleep(2)
        
        textField_3 = pe.getElement('inputs', 'class_name')
        textField_3.clear()
        textField_3.send_keys('Test_3')
        time.sleep(2)
        
        driver.quit()

run_test = UsingWrapers()
run_test.test() 