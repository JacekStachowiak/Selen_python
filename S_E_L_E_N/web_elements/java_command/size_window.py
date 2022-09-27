import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class WindowSize():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://courses.letskodeit.com/practice')
        driver.implicitly_wait(4)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print(f'Height window is: {height}')
        print(f'Width window is: {width}')
       
        driver.quit()

run_test = WindowSize()
run_test.test()  