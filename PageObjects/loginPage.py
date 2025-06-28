# pageObjects/LoginPage.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_input = ("//input[@placeholder='Username']")
    password_input = ("password")
    login_button   = ("//button[@type='submit']")

    # Actions
    def setUsername(self, username):
        self.driver.find_element(By.XPATH,self.username_input).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME,self.password_input).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button).click()