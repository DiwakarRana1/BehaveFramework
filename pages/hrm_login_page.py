from utility.locators import PageLocators
from utility.web_page_actions import WebPageActions


class HrmLoginPage(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.hrm_username_locator = PageLocators.HrmUsername
        self.hrm_password_locator = PageLocators.HrmPassword
        self.hrm_login_button_locator = PageLocators.HrmSubmit


    def enter_credentials(self):
        """Enter the Username and Password From Config file"""
        self.enter_text_from_config(self.hrm_username_locator, "Username")
        self.enter_text_from_config(self.hrm_password_locator,"Password")

    def click_on_login_button(self):
        """Click on Login Button"""
        self.click_element(self.hrm_login_button_locator)

