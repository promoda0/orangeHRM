import pytest

from Pages.login import LoginPage  # Your Page Object class

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_valid_login(self):
        """Test successful login"""
        self.login_page.login("Admin", "admin123")
        assert "dashboard" in self.driver.current_url.lower()

    def test_invalid_login(self):
        """Test invalid credentials"""
        self.login_page.login("invalid_user", "wrong_password")
        error_text = self.login_page.get_error_message()
        assert "Invalid credentials" in error_text


