import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class SlidersAction():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://jqueryui.com/slider/'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        driver.switch_to.frame(0)   # ustawiamy frame-ma
        
        element = driver.find_element(By.XPATH, '//div[@id="slider"]')
        time.sleep(3)
        
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()    # source x =100, y = 0
            time.sleep(3)
            print('Sleding Element successful')
            time.sleep(2)
        except:
            print('Sliding failed on element')
                         
        driver.quit()
    
    
run_test = SlidersAction()
run_test.test()

            