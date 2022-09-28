# wyskakujące pop_up nie widać w inspektorze
# oneclick = diframe-nameisplayAlert()
# oneclick = displayConfirm()
# szukamy javascript

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# najpierw przełączamy sie iframe a potem połączyć

class SwitchToFrame_2():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        driver.find_element(By.ID, 'name').send_keys('jac')
        alert = driver.find_element(By.ID, 'alertbtn')
        alert.click() # alert jest zawsze java
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept() # click-amy
        time.sleep(3)
        
        driver.find_element(By.ID, 'name').send_keys('jac')
        confirm = driver.find_element(By.ID, 'confirmbtn')
        confirm.click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        # alert2.accept() # OK
        alert2.dismiss() # cancel
        time.sleep(3)
       
        driver.quit()

run_test = SwitchToFrame_2()
run_test.test()  
