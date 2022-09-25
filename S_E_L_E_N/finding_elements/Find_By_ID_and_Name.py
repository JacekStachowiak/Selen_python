from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FindByIdName():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        elementById = driver.find_element(By.ID, 'displayed-text')
        #sprawdzamy czy element jest
        if elementById is not None:
            print('Element znaleziono --> By.ID')

        elementByName = driver.find_element(By.NAME, 'show-hide')
        if elementByName is not None:
            print('Element znaleziono --> By.Name')
        
        driver.close()

run_test = FindByIdName()
run_test.test()
# id może być dynamiczne i pop ponownym otwarciu przeglądarki test nie przejdzie - przykład strona Yahoo.com