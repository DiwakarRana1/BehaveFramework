from utility.locators import PageLocators
from utility.web_page_actions import WebPageActions
import time


class HrmLoginPage(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.hrm_username_locator = PageLocators.HrmUsername
        self.hrm_password_locator = PageLocators.HrmPassword
        self.hrm_login_button_locator = PageLocators.HrmSubmit
        self.hrm_password_locator_list = PageLocators.HrmPassword_list


    def enter_credentials(self):
        """Enter the Username and Password From Config file"""
        print("Entering username...")
        self.enter_text_from_config(self.hrm_username_locator, "Username")
        print("Entering password...")
        self.enter_text_from_config(self.hrm_password_locator_list,"Password")
        print("Credentials entered successfully")



    def click_on_login_button(self):
        """Click on Login Button"""
        print("Attempting to click login button...")
        # Try to find the button first to verify it exists
        try:
            button = self.driver.find_element(*self.hrm_login_button_locator)
            print(f"Login button found: {button.is_displayed()}, {button.is_enabled()}")
            print(f"Button text: {button.text}")
            print(f"Button HTML: {button.get_attribute('outerHTML')}")
        except Exception as e:
            print(f"Error finding login button: {e}")
        
        # Now try to click it
        self.click_element(self.hrm_login_button_locator)
        print("Login button clicked")
        # Add a small wait after clicking
        time.sleep(1)

