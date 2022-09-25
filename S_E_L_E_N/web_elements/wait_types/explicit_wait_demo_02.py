from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from explicit_wait_type import ExplicitWaitType

# nigdy nie mieszaj oby implicity i WebDriverWait

class ImplicityWaitDemo2():
    
    def test(self):
                
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)      

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator='//a[text()="Sign In"]', locatorType='xpath', timeout_1=50, pollFrequency_1=0.5) # wartości takie same jak w def można pominąć
        element.click()
      
        time.sleep(2)       
        driver.quit()

run_test = ImplicityWaitDemo2()
poczatek = time.time()
run_test.test() 
koniec = time.time()

print(f'Pomiar Implicity to: {round(koniec - poczatek,3)}')
