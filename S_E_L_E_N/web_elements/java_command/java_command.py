import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class JavaScript():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        # driver.get('https://courses.letskodeit.com/practice')
        driver.execute_script("window.location = 'https://courses.letskodeit.com/practice';") # java
        driver.implicitly_wait(10)

        # element = driver.find_element(By.ID, 'name')
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys('Test')
        time.sleep(2)
       
        driver.quit()

run_test = JavaScript()
run_test.test()        