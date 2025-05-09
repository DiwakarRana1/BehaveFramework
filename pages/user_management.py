from utility.locators import PageLocators
from utility.web_page_actions import WebPageActions
import time


class UserManagement(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.usm_login_button_locator = PageLocators.UsmLogin
        self.usm_email_locator = PageLocators.UsmEmail
        self.usm_password_locator = PageLocators.UsmPassword
        self.usm_login_submit_locator = PageLocators.UsmLoginSubmit

    def click_on_usm_login_button(self):
        """Click on Login Button"""
        print("Attempting to click login button...")
        # Try to find the button first to verify it exists
        try:
            button = self.driver.find_element(*self.usm_login_button_locator)
            print(f"Login button found: {button.is_displayed()}, {button.is_enabled()}")
            print(f"Button text: {button.text}")
            print(f"Button HTML: {button.get_attribute('outerHTML')}")
        except Exception as e:
            print(f"Error finding login button: {e}")

        # Now try to click it
        self.click_element(self.usm_login_button_locator)
        print("Login button clicked")
        # Add a small wait after clicking
        time.sleep(1)

    def enter_usm_credentials(self):
        """Enter the Email and Password From Config file"""
        print("Entering Email...")
        self.enter_text_from_config(self.usm_email_locator, "User_Email")
        print("Entering password...")
        self.enter_text_from_config(self.usm_password_locator, "User_Password")
        print("Credentials entered successfully")

    def click_on_usm_submit_button(self):
        """Click On Login button"""
        print("Clicking on Login Button...")
        self.click_element(self.usm_login_submit_locator)
        time.sleep(1)
