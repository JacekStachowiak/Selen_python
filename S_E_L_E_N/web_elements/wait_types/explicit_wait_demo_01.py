# klikanie i selected to 2 najważniejsze do czekania
# title, visibility_of_element_lacated

# timeout - ile czasu czekać zanim powiem, że nie ma elementu  - np. 20 sek
# poll_frequency - częstotliwość np. przez 20 sek co 1 sek
# ignored_exception - ignorowane wyjątki w podanym czasie czekania
# element = wait.until(EC.element_to_be_clikable(by Type, locator)) np By.ID, locator

from timeit import Timer
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait     # wait
from selenium.webdriver.support import expected_conditions as EC    # oczekiwane elementy
from selenium.common.exceptions import *    # obsługa wyjątków

class ImplicityWaitDemo():
    
    def test(self):
                
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)       # ten driver czeka na załadowanie strony i clicka - chyba, że jest bardzo wolny internet
        driver.implicitly_wait(10)
        
        driver.find_element(By.XPATH, '//a[text()="Sign In"]').click()
       
        time.sleep(2)       
        driver.quit()

run_test = ImplicityWaitDemo()
poczatek = time.time()
run_test.test() 
koniec = time.time()

class ExplicitWaitDemo():
    
    def test(self):
        
        # baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        # driver.get(baseUrl)       # ten driver czeka na załadowanie strony i clicka - chyba, że jest bardzo wolny internet
        driver.execute_script('window.location = "https://courses.letskodeit.com/";') # ten driver nie czeka na nic
        # driver.find_element(By.XPATH, '//a[text()="Sign In"]').click()
        
        # czas oczekiwania, częstotliwość, lista wyjątków - tu 3 najczęściej, ale są inne. Nie będzie czekał 20s tylko do czasu aż element się pojawi        
        wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotSelectableException]) 
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Sign In"]'))) # uwaga na ilośc nawiasów
        element.click() # zostawiamy script java bo otwiera bez czekania 
        
        time.sleep(2)       
        driver.quit()

run_test = ExplicitWaitDemo()
poczatek2 = time.time()
run_test.test() 
koniec2 = time.time()

print(f'Pomiar Implicity to: {round(koniec - poczatek,3)}')
print(f'Pomiar Excplicit to: {round(koniec2 - poczatek2,3)}')


