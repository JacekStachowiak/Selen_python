import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# chcę spr czy jest text na button zawsze pomiedzy tag-ami <a ....   >"Open Tab"</a>

class TextElements():
    
    def test_get_text(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        openTab = driver.find_element(By.ID, 'opentab')
        elementText = openTab.text      # pobieramy text
        print(f'Text on element is: "{elementText}"')     # Text on element is: "Open Tab"
                
        driver.quit()

run_test = TextElements()
run_test.test_get_text()         