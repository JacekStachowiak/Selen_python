import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

# najeżdżamy myszką na "Mouse Hover" i wyświtla się menu

class MouseHoverAction():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        element = driver.find_element(By.ID, 'mousehover')
        clickLocator = '//div[@class="mouse-hover-content"]//a[text()="Top"]'
        
                
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('Mouse hovered on element')
            time.sleep(3)
            topLink = driver.find_element(By.XPATH, clickLocator)
            actions.move_to_element(topLink).click().perform()
            print('Item Top clicked')
        except:
            print('Mouse hovered failed on element')

        driver.quit()
        
    def test_2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(4)
        
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        element = driver.find_element(By.ID, 'mousehover')
        clickLocator_2 = '//div[@class="mouse-hover-content"]//a[text()="Reload"]'
                
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('Mouse hovered on element')
            time.sleep(3)
            topLink = driver.find_element(By.XPATH, clickLocator_2)
            actions.move_to_element(topLink).click().perform()
            print('Item Reload clicked')
        except:
            print('Mouse hovered failed on element')
        
        driver.quit()

run_test = MouseHoverAction()
run_test.test()  
run_test.test_2()      