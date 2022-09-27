import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SwitchToWindow():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        # find parrent handle --> Main Window
        parentHandle = driver.current_window_handle
        print(f'Parent handle: {parentHandle}')
                
        # Find open window button and click()
        driver.find_element(By.ID, 'openwindow').click()
        time.sleep(2)
        
        # find all handle
        handles = driver.window_handles
        
        # switch to windows and search course
        for handle in handles:
            print(f' Handle: {handle}')
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print(f'Switched to window: {handle}')
                search = driver.find_element(By.ID, 'search')
                search.send_keys('python')
                time.sleep(3)
                driver.close()   
                break
        
        # back to parentHandle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, 'name').send_keys('Test success')
        
        driver.quit()

run_test = SwitchToWindow()
run_test.test()  