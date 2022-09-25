import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# radiobutto - tylko jeden wybór - type radio
# checkbox - kilka wyborów  - type checkbox
# input - wpisujemy dane - type text

class Find_button():
    
    def button_radio(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        bmwRadioBtn = driver.find_element(By.ID, 'bmwradio')
        bmwRadioBtn.click()
        
        time.sleep(3)
        benzRadioBtn = driver.find_element(By.ID, 'benzradio')
        benzRadioBtn.click()
        
        time.sleep(3)
        benzCheckBox = driver.find_element(By.ID, 'benzcheck')
        benzCheckBox.click()
        
        time.sleep(2)
        hondaCheckBox = driver.find_element(By.ID, 'hondacheck')
        hondaCheckBox.click()
        
        time.sleep(3)
        
        # sprawdzamy czy jest wybrany czy nie
        print(f'Czy został wybrany radio button BMW {bmwRadioBtn.is_selected()}')
        print(f'Czy został wybrany radio button Benz {benzRadioBtn.is_selected()}')
        print(f'Czy został wybrany checkbox Benz {benzCheckBox.is_selected()}')
        print(f'Czy został wybrany checkbox Honda {hondaCheckBox.is_selected()}')
        
        driver.quit()
       
run_test = Find_button()
run_test.button_radio()
       
        