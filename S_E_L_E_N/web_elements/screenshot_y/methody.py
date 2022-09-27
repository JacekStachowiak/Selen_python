from fileinput import filename
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait     # wait
from selenium.webdriver.support import expected_conditions as EC    # oczekiwane elementy
from selenium.common.exceptions import *    # obsługa wyjątków

class Screenshots():
    
    def test(self):
                
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)      
        driver.implicitly_wait(3)
        
        driver.find_element(By.XPATH, '//a[text()="Sign In"]').click()       
        driver.find_element(By.ID, 'email').send_keys('abc@email.com')       
        driver.find_element(By.ID, 'password').send_keys('abc')
        driver.find_element(By.XPATH, '//input[@class="btn btn-default btn-block btn-md dynamic-button"]').click()
        self.takeScreenshots(driver)
        
        driver.quit()

    def takeScreenshots(self, driver):
        
        fileName = str(round(time.time()*1000)) + '.png'    # losowa nazwa pliku
        screenshotsDirectory = 'H:\\Git_projekty\\Udemy_selen_python\\S_E_L_E_N\\web_elements\\screenshot_y\\' # miejsce zapisu
        destinationFile = screenshotsDirectory + fileName   

        try:
            driver.save_screenshot(destinationFile)
            print(f'Screenshots save to directory: {destinationFile} ')
        except NotADirectoryError:
            print('Not a diretory issue')
    
        driver.quit()
            
run_test = Screenshots()
run_test.test()        