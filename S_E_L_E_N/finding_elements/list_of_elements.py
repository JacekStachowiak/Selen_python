from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# jak znależć wszystkie elementy na stronie np. tekstowe, przyciski, o tej samej nazwie tag-u itp
# elementy które mają ten sam atrybut w tym samym czasie, elementy wejściowe klasy, wszystkie div-y 
# //input[@class="inputs"] - 2 elementy maja taką samą class-ę

class ListOfElements():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        
        # I sposób
        elementListByClassName = driver.find_elements(By.CLASS_NAME, 'inputs')
        length1 = len(elementListByClassName)
        #sprawdzamy czy element jest
        if elementListByClassName is not None:
            print(f'Rozmiar listy ClassName inputs: {str(length1)}')   # Rozmiar listy ClassName inputs: 3


        elementListByClassName = driver.find_elements(By.CLASS_NAME, 'btn-style')
        length5 = len(elementListByClassName)
                
        if elementListByClassName is not None:
            print(f'Rozmiar listy ClassName btn-style: {str(length5)}')


        # II sposób
        elementListByTagName = driver.find_elements(By.TAG_NAME, 'h1')  # dowolny tag
        length2 = len(elementListByTagName)
        
        if elementListByTagName is not None:
            print(f'Rozmiar listy TagName h1: {str(length2)}') # Rozmiar listy TagName h1: 1
        
        
        elementListByTagName = driver.find_elements(By.TAG_NAME, 'td')  # Rozmiar listy TagName td: 9
        length3 = len(elementListByTagName)
        
        if elementListByTagName is not None:
            print(f'Rozmiar listy TagName td: {str(length3)}') # Rozmiar listy TagName: 1
        
        
        elementListByTagName = driver.find_elements(By.TAG_NAME, 'tr')  # Rozmiar listy TagName td: 9
        length4 = len(elementListByTagName)
        
        if elementListByTagName is not None:
            print(f'Rozmiar listy TagName tr: {str(length4)}') # Rozmiar listy TagName: 1
        
        
        elementListXpath = driver.find_elements(By.XPATH, '//div[@id="page"]')
        length7 = len(elementListXpath)
                
        if elementListXpath is not None:
            print(f'Rozmiar listy Xpath //div[@id="page"]: {str(length7)}')
        
        
        
        driver.close()

run_test = ListOfElements()
run_test.test()