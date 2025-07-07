from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.username_field = (By.XPATH, "//label[text()='Username']/following::input[1]")
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-wrapper')]")
        self.user_role_options = (By.XPATH, "//div[@role='listbox']//span")
        self.emp_name_field = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-wrapper')]")
        self.status_options = (By.XPATH, "//div[@role='listbox']//span")
        self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.result_rows = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    def click_admin_menu(self):
        self.driver.find_element(*self.admin_menu).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def select_user_role(self, role_name):
        self.driver.find_element(*self.user_role_dropdown).click()
        roles = self.driver.find_elements(*self.user_role_options)
        for role in roles:
            if role.text.strip() == role_name:
                role.click()
                break

    def enter_employee_name(self, emp_name):
        emp_input = self.driver.find_element(*self.emp_name_field)
        emp_input.clear()
        emp_input.send_keys(emp_name)
        emp_input.send_keys(Keys.ENTER)  # select the suggested user from dropdown

    def select_status(self, status):
        self.driver.find_element(*self.status_dropdown).click()
        statuses = self.driver.find_elements(*self.status_options)
        for stat in statuses:
            if stat.text.strip() == status:
                stat.click()
                break

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def is_result_found(self):
        return len(self.driver.find_elements(*self.result_rows)) > 0
