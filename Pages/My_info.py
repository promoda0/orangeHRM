import logging
import time

from selenium.webdriver.common.by import By

from Base.base_page import BasePage

class myinfo(BasePage):

    #Locator for This page

    my_info_button = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[6]"
    Xpath_Firstname = "//input[@class='oxd-input oxd-input--active orangehrm-firstname']"
    Xpath_middle_name = "//input[@class='oxd-input oxd-input--active orangehrm-middlename']"
    Xpath_lastname = "//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
    Xpath_Employee_id = "(//input[@class ='oxd-input oxd-input--active'])[2]"
    Xpath_other_id="(//input[@class='oxd-input oxd-input--active'])[3]"
    Xpath_Driver_License_Number="(//input[@class='oxd-input oxd-input--active'])[4]"
    Xpath_License_Expiry_Date="(//input[@class='oxd-input oxd-input--active'])[5]"
    Xpath_select_country = "//div[@class='oxd-select-text-input']"




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        logging.info("Initialized Login Page")
        self.my_info_button = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[6]")
        self.Xpath_Firstname = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")

    def Update_Personal_Details(self,data_file_path='TestCases/testdata/Employee_info.json'):

        self.click(self.my_info_button)
        data = self.load_test_data(data_file_path)
        logging.info("Updating Personal Details")

        self.clear_field(self.Xpath_Firstname)
        time.sleep(5)
        """
        self.send_keys(self.Xpath_Firstname,data["First_name"])
        logging.info("Enter the first name")
        self.send_keys( self.Xpath_middle_name, data["Middle_name"])
        self.send_keys( self.Xpath_lastname,data["Last_name"])
        self.send_keys( self.Xpath_Employee_id,data["Employee_id"])
        self.send_keys( self.Xpath_other_id, data["Employee_other-id"])
        self.send_keys( self.Xpath_Driver_License_Number, data["Driver_License_Number"])
        self.send_keys( self.Xpath_License_Expiry_Date, data["License_Expiry_Date"])

    """