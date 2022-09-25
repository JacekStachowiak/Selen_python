from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class BrowserInteraction():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()

        title = driver.title
        print(f'To jest tytuł strony: {title}')         # To jest tytuł strony: Practice Page
        currentUrl = driver.current_url
        print(f'Current URL tej strony: {currentUrl}')  # Current URL tej strony: https://courses.letskodeit.com/practice
        driver.refresh()
        print('Driver refresh 1-st time')
        driver.get(driver.current_url)
        print('Driver refresh 2-st time')
        driver.get('https://courses.letskodeit.com/')
        currentUrl = driver.current_url
        print(f'Current URL tej strony: {currentUrl}')
        driver.back()
        currentUrl = driver.current_url
        print(f'Current URL tej strony: {currentUrl}')
        print('Wracamy na stronę poprzednią')
        driver.forward()
        currentUrl = driver.current_url
        print(f'Current URL tej strony: {currentUrl}')
        print('Przechodzimy na stronę do przodu')
        pageSource = driver.page_source
        #print(pageSource)  # wydruk całej strony html
                

        driver.quit()

run_test = BrowserInteraction()
run_test.test()        