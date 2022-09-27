import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class ScrollPage():
    
    def test(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://courses.letskodeit.com/practice')
        driver.implicitly_wait(4)
        time.sleep(3)
        
        # scroll down
        driver.execute_script("window.scrollBy(0,924);")    # poziom i drugi: zakres dokąd
        time.sleep(3)
        
        # scroll up
        driver.execute_script("window.scrollBy(0,-924);")
        time.sleep(3)
        
        # scroll element into view
        element = driver.find_element(By.ID, 'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")
        
        # native way to scroll element into view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-924);")
        location = element.location_once_scrolled_into_view
        print(f'location: {str(location)}') # location: {'x': 394, 'y': 0}
       
        driver.quit()

run_test = ScrollPage()
run_test.test()  