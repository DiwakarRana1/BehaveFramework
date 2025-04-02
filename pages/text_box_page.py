from utility.web_page_actions import WebPageActions
from utility.locators import PageLocators

class TextBoxPage(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.full_name_locator = PageLocators.FullName
        self.email_locator = PageLocators.Email
        self.current_address_locator = PageLocators.CurrentAddress
        self.permanent_address_locator = PageLocators.PermanentAddress
        self.submit_button_locator = PageLocators.SubmitButton
        self.text_box_page_locator = PageLocators.textBox

    def click_on_text_box(self):
        """Click on Side Menu for Text Box"""
        self.click_element(self.text_box_page_locator)


    def fill_text_fields(self):
        """Enter the values from the config file to all the fields"""
        self.enter_text_from_config(self.full_name_locator, "Full Name")
        self.enter_text_from_config(self.email_locator, "Email")
        self.enter_text_from_config(self.current_address_locator, "Current Address")
        self.enter_text_from_config(self.permanent_address_locator, "Permanent Address")

    def submit_button_click(self):
        """Click on the submit button"""
        self.click_element(self.submit_button_locator)
