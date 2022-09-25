from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FindByLinkText():
    
    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        elementByLinkText = driver.find_element(By.LINK_TEXT, 'HOME')
        # to jest text z linku który klikamy na stronie - pełny zawsze z tag a
        if elementByLinkText is not None:
            print('Element znaleziono --> By.LinkText')

        elementByPatrialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, 'COURSES')
        # to jest text z linku który klikamy na stronie - częściowy tekst zawsze z tag a
        if elementByPatrialLinkText is not None:
            print('Element znaleziono --> By.PatrialLinkText')
        
        driver.close()

run_test = FindByLinkText()
run_test.test()