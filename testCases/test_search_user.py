import time

import pytest
from PageObjects.loginPage import LoginPage
from PageObjects.adminPage import AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestSearchUser:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_search_user_with_multiple_filters(self, setup):
        self.logger.info("=== Test_001_Login Started ===")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to: {self.baseURL}")
        self.driver.implicitly_wait(10)

        # Login
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.lp.setUsername(self.username)
        self.logger.info("Entered Username")

        self.lp.setPassword(self.password)
        self.logger.info("Entered Password")

        self.lp.clickLogin()
        self.logger.info("Clicked Login Button")

        # Wait for Admin menu
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))

        # Admin Page
        admin = AdminPage(self.driver)
        admin.click_admin_menu()

        # Wait for Search filters to load
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Search']")))

        # Apply Search Filters
        admin.enter_username("Admin")
        admin.select_user_role("ESS")
        admin.enter_employee_name("manda user")
        admin.select_status("Enabled")

        # Click Search
        admin.click_search_button()

        # Wait for results
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")))

        # Validate search result
        assert admin.is_result_found(), "No records found for the given filters."

        self.driver.close()
