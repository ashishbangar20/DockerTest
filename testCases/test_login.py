# testCases/test_001_Login.py
import os

import pytest
from PageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):

        self.logger.info("=== Test_001_Login Started ===")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to: {self.baseURL}")
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.logger.info("Entered Username")

        self.lp.setPassword(self.password)
        self.logger.info("Entered Password")

        self.lp.clickLogin()
        self.logger.info("Clicked Login Button")

        if "OrangeHRM" in self.driver.title:
            self.logger.info("Login Test Passed")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\test_account_reg.png")
            self.logger.error("Login Test Failed")
            assert False