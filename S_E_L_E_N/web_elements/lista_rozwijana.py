import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

# //option[@value='bmw'] - wybraliśmy jeden element (a jak będzie 500 ?)
# zadzaiała tylko na tagu select - trzeba spr
# 3 sposoby
#


class Select_list():
    
    def test(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        el1 = driver.find_element(By.ID, 'carselect') # z tagu select
        sel = Select(el1)
        
        time.sleep(2)
        sel.select_by_value('benz')
        print('Select Benz by value')
        time.sleep(2)
        
        sel.select_by_index('2')    # 3 na liście (liczymy od zera)
        print(f'Select Honda by index')
        time.sleep(1)
        
        sel.select_by_visible_text('BMW')   # text wg listy
        print(f'Select BMW by visible text')
        time.sleep(2)
        
        sel.select_by_index(2)
        print(f'Select Honda by index - drugi sposób')
                
        driver.quit()
       
run_test = Select_list()
run_test.test()    