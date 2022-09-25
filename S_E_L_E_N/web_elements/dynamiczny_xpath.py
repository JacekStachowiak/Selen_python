import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# //h4[contains(@class, 'dynamic-heading')] znajduje 3 elementy
# //h4[contains(@class, 'dynamic-heading') and contains(text(), 'JavaScript for beginners ')] - elementów zero
# 

class DynamicXpath():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
    
        # how to click and type on e web element
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        email = driver.find_element(By.ID, 'email')
        email.send_keys('test@email.com')
        password = driver.find_element(By.ID, 'password')
        password.send_keys('abcabc')
        driver.find_element(By.XPATH, '//input[@class="btn btn-default btn-block btn-md dynamic-button"]').click()
        driver.find_element(By.XPATH, '//a[contains(@class,"dynamic-link") and contains(text(), "ALL COURSES")]').click()
        
        # search for courses
        searchBox = driver.find_element(By.XPATH, '//input[@id="search"]')
        searchBox.clear()
        searchBox.send_keys('JavaScript')
        searchBox.click()
        
        # Select Course
        _course = '//h4[contains(@class, "dynamic-heading") and contains(text(), "{0}")]' # zamiast tytułu wstawiamy {0}
        _courseLocator = _course.format('JavaScript for beginners')     # tytuł wstawiamy tu
        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(4)
        '''
        _course = '//h4[contains(@class, "dynamic-heading") and contains(text(), "{0}{1}")]' # zamiast tytułu wstawiamy {0}
        _courseLocator = _course.format('JavaScript for beginners', 'drugi tytuł') 
        
        '''
        driver.quit()

run_test = DynamicXpath()
run_test.test()         