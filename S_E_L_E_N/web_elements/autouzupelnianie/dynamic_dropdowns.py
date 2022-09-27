import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC   
from selenium.common.exceptions import *

# aby zatrzymać listę punkt przerwania

class AutoComplite():
    
    def test(self):
        
        baseUrl = 'https://www.expedia.com'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        patrialText = 'pol'
        textToSelect = 'Kraków (KRK - John Paul II-Balice)' # wpisujemy dokładnie z print(element.text)
        
        flight = driver.find_element(By.XPATH, '//span[text()="Flights"]')
        flight.click()
        
        textElement = driver.find_element(By.XPATH, '//div[@id="location-field-leg1-origin-menu"]//button') 
        textElement.send_keys(Keys.ENTER, patrialText)
        time.sleep(5)
        
        # z listy wybieramy
        # xpath
        # tag_name wspólny dla wszystkich
        # class_name wspólna dla wszystkich
        
        ulElement = driver.find_element(By.CLASS_NAME, 'uitk-typeahead-result-item has-subtext')
        inner_html = ulElement.get_attribute('innerHtml')
        # inner_text = ulElement.get_attribute('innerText')) # jeżeli nie działa wyżej
        print(inner_html)
        
        liElements = ulElement.find_elements(By.TAG_NAME, 'li')
        time.sleep(2)
        
        for element in liElements:
            # print(element.text)
            if textToSelect in element.text:
                element.click()
                break
            
        time.sleep(4)    
        driver.quit()

run_test = AutoComplite()        
run_test.test()