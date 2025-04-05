import time

import pytest

from Pages.login import LoginPage  # Your Page Object class
from Pages.My_info import myinfo
class TestLogin:




    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.myinfo = myinfo(self.driver)

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_my_info(self):
        """My info page test"""
        self.login_page.login("Admin", "admin123")
        time.sleep(5)
        self.myinfo.Update_Personal_Details()
