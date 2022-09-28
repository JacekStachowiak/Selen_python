import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# najpierw przełączamy sie iframe a potem połączyć

class SwitchToFrame():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.execute_script("window.scrollBy(0,924);")
        
        # I sposób - switch to frame using id - przełaczamy się do iframe
        # driver.switch_to.frame('courses-iframe') 
        
        # II sposób - switch to frame using name
        # driver.switch_to.frame('iframe-name') 
        
        # III sposób - switch to frame using numbers - zero bo mamy na stronie tylko jedną iframe - zaczyna się od 0
        driver.switch_to.frame(0) 
        
        time.sleep(2)
        
        # Search course
        searchBox = driver.find_element(By.XPATH, '//input[@id="search"]')
        searchBox.send_keys('python', Keys.ENTER)
        time.sleep(2)
        
        # switch back to the parent frame - wracamy do domyslnego frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-924);")
        driver.find_element(By.ID, 'name').send_keys('Test udany !!!')
        time.sleep(3)

        driver.quit()

run_test = SwitchToFrame()
run_test.test()  