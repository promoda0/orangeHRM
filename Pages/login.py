from selenium.webdriver.common.by import By
from Base.base_page import BasePage
import logging

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        logging.info("Initialized Login Page")

    def login(self, username, password):
        """Perform login with credentials"""
        logging.info(f"Attempting login with username: {username}")
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def login_with_invalid_credentials(self, username, password):
        """Perform login expecting failure"""
        logging.info(f"Attempting invalid login with username: {username}")
        self.login(username, password)
        return self.get_error_message()

    def get_error_message(self):
        """Get login error message text"""
        try:
            message = self.get_text(self.ERROR_MESSAGE)
            logging.warning(f"Login error message detected: {message}")
            return message
        except:
            logging.info("No error message present")
            return None

    def is_login_successful(self):
        """Verify successful login"""
        try:
            return self.is_element_visible(self.DASHBOARD_HEADER)
        except:
            return False