# podnieść i upuść

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

# najeżdżamy myszką na "Mouse Hover" i wyświtla się menu

class DragAndDropAction():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://jqueryui.com/droppable/'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        driver.switch_to.frame(0)   # ustawiamy frame-ma
        
        fromElement = driver.find_element(By.ID, 'draggable')
        toElement = driver.find_element(By.ID, 'droppable')
        time.sleep(3)
        
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            print('Drag and Drop element successful')
            time.sleep(2)
        except:
            print('Drag and Drop failed element')
                         
        driver.quit()

run_test = DragAndDropAction()
run_test.test()
            