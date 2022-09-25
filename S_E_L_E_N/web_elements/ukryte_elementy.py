import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# //input[@id='displayed-text'] widzimy
# po wcisnięciu hide element ze strony znika, ale w xpath jest
# style="display: none;"    niewidoczny - kod sie wykona, ale jak będziemy chcieli wykonać działanie to będzie wyjątek
# style="display: block;"  widoczny
# oba w tym przypadku są cały czas - widoczne lub nie
# zdarza się jednak że dane pole znika i poprzedni xpath już go nie widzi
# istniejacy/nie istniejący  lub  widoczny/nie widoczny

# //input[@id='hide-textbox']
# //input[@id='show-textbox']

class HiddenElements():
    
    def test_letskodeit(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)
        
        # stan pola text-owego - sprawdzamy czy pole textowe jest wyświetlane czy nie
        textBoxElement = driver.find_element(By.ID, 'displayed-text')
        textBoxState = textBoxElement.is_displayed()   # czy jest wyświetlany True/False
        print(f'Text is visible?: {textBoxState}')
        time.sleep(3)
        
        # kliknij w button hidden
        driver.find_element(By.ID, 'hide-textbox').click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()   
        print(f'Text is visible?: {textBoxState}')
        time.sleep(3)
        
        # kliknij w button show
        driver.find_element(By.ID, 'show-textbox').click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()   
        print(f'Text is visible?: {textBoxState}')
        time.sleep(3)
        
        driver.quit()
        
    def test_expedia(self):
        
        baseUrl = 'https://www.expedia.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)
        
        driver.find_element(By.ID, 'tab-flight-tab').click()
        
        drpdwnElement = driver.find_element(By.ID, 'flight-age-select-1')
        print(f'Element is visible? {drpdwnElement.is_displayed()}')

        driver.quit()

run_test = HiddenElements()
run_test.test_letskodeit()  
# run_test.test_expedia()       