# klikanie i selected to 2 najważniejsze do czekania
# title, visibility_of_element_lacated

# timeout - ile czasu czekać zanim powiem, że nie ma elementu  - np. 20 sek
# poll_frequency - częstotliwość np. przez 20 sek co 1 sek
# ignored_exception - ignorowane wyjątki w podanym czasie czekania
# element = wait.until(EC.element_to_be_clikable(by Type, locator)) np By.ID, locator

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class ImplicityWaitDemo():
    
    def test(self):
        
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10) # tu jest długi czas (nie jawny) dla każdej operacji - potrzebujemy tylko dla emailField
                
        loginLink = driver.find_element(By.XPATH, '//div[@id="navbar-inverse-collapse"]//a[@href="/login"]')
        loginLink.click()
        
        emailField = driver.find_element(By.ID, 'email')
        emailField.send_keys('test')
        time.sleep(3)
        
        driver.quit()

run_test = ImplicityWaitDemo()
run_test.test() 


