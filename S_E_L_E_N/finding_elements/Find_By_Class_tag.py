import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FindByClassTag():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        elementByClassName = driver.find_element(By.CLASS_NAME, 'inputs')
        #class=btn-style class2   oznacza, że mamy 2 klasy i możemy podać tylko jedną
        if elementByClassName is not None:
            print('Element znaleziono --> By.ClassName')
            elementByClassName.send_keys('Testing')

        elementByTagName = driver.find_element(By.TAG_NAME, 'a')
        if elementByTagName is not None:
            print(f'Element znaleziono --> By.TagName: {elementByTagName.text}') # po tagu text wyciagamy tekst
        
        time.sleep(3)
        
        driver.close()

run_test = FindByClassTag()
run_test.test()