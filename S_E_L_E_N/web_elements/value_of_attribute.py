from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# chcę spr jaka jest wartość atrybutu danego elementu 
# <input(element) -->  id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text" xpath="1">(reszta to atrybuty i ich wartości)

class AttributeElements():
    
    def test_value_attribute(self):
        
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        element = driver.find_element(By.ID, 'name')
        result = element.get_attribute('class')             # pobieramy atrybut klasy
        print(f'Wartosc attribute class is: "{result}"')    # Wartosc attribute class is: "inputs"
        
        result_2 = element.get_attribute('placeholder')
        print(f'Wartosc attribute placeholder is: "{result_2}"')   # Wartosc attribute placeholder is: "Enter Your Name"
        
        result_3 = element.get_attribute('type')
        print(f'Wartosc attribute type is: "{result_3}"')    # Wartosc attribute type is: "text"
                
        driver.quit()

run_test = AttributeElements()
run_test.test_value_attribute() 