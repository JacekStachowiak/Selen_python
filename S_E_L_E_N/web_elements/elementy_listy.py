import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# jak sprawdzić całą listę radio_button's czy istnieją
# wszystkie mają wspólne: name = cars i type = radio
# //input[@type='radio'] ale w pewnych sytuacjach to za mało
# //input[contains(@type, 'radio') and contains(@name, 'cars')]

class Find_list():
    
    def test_of_elements_list(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
                
        radioButtonList = driver.find_elements(By.XPATH, '//input[contains(@type, "radio") and contains(@name, "cars")]')
        size = len(radioButtonList)
        print(f'Ilość elementów radio button to: {size}')   # Ilość elementów radio button to: 3
        
        for radio_button in radioButtonList:
            isSelected = radio_button.is_selected()
            # jeżeli nie wybrany to wybierz
            if not isSelected:
                radio_button.click()
                time.sleep(2)
                
        driver.quit()
       
run_test = Find_list()
run_test.test_of_elements_list()        