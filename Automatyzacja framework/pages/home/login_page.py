from selenium.webdriver.common.by import By
class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
    
    # locators
    _login_link = '//a[text()="Sign In"]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _all_Course = '//a[text()="ALL COURSES"]'
    
    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, self._login_link)
    
    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)
    
    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)
    
    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)
    
    def getAllCourse(self):
        return self.driver.find_element(By.XPATH, self._all_Course)
    
    
    def clickLoginLink(self):
        self.getLoginLink().click()
    
    def enterEmail(self, email):
        self.getEmailField().send_keys(email)
    
    def enterPassword(self, password):
        self.getPasswordField().send_keys(password) 
    
    def clickLoginButton(self):
        self.getLoginButton().click()
    
    def clickAllCourse(self):
        self.getAllCourse().click()


    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.clickAllCourse()
