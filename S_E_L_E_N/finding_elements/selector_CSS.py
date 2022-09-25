from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# input[id="displayed-text"]
# # --> Id
# #displayed-text  - to samo co wyżej skrót do Id
# input#displayed-text
# . --> class
# input.inputs
# input.displayed-class
# .displayed-class
# input[class='inputs displayed-class'] tutaj dodajemy inputs
# input[class='inputs']     2 elementy posiadają
# input[class^='inputs']    3 elementy zaczynają się od inputs
# input[class^='inp']   zaczyna się od inp 
# input[class='displayed-class']    nic nie znalazł musiałoby być input[class='inputs displayed-class']
# input[class$='displayed-class']   gdy class kończy się na displayed-class w tag input
# input[class$='class'] możemy skrócić tylko końcową nazwę
# input[placeholder='Enabled/Disabled Field']
# input[placeholder^='Enabled']
# input[placeholder$='Field']

# input[placeholder*='Disabled'] dowolne miejsce
# input[class='btn-style class2']
# input[class*='style']

# element ma wiele klas
# .inputs.displayed-class
# .btn-style - 9 elementów (zielone przyciski)
# .btn-style.class1 
# .btn-style.class1.class2 
# .btn-style.class2.class1 - to samo 

# szukanie dzieci children
# fieldset>table znajdzie 1 tabelę bo jest tylko jedna
# #product
# fieldset>#product    to jest ten zapis (table id="product")

class ListOfElements():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()

        