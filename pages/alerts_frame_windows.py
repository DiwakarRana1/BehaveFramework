from utility.web_page_actions import WebPageActions
from utility.locators import PageLocators
from utility.tab_handler import TabHandler

class NewTabPage(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.new_tab_button_locator = PageLocators.NewTabButton
        self.alert_menu = PageLocators.AlertMenu
        self.browser_menu = PageLocators.BrowserMenu
        self.tab_handler = TabHandler(driver)  # Initialize tab handling

    def click_on_alert_menu(self):
        """Click on the Alert Menu to get the dropdown for Browser Menu"""
        self.click_element(self.alert_menu)

    def click_on_browser_menu(self):
        """Click on Browser Menu"""
        self.click_element(self.browser_menu)

    def click_on_new_tab_button(self):
        """Click the button to open a new tab."""
        self.click_element(self.new_tab_button_locator)

    def switch_to_new_tab(self):
        """Switch to the newly opened tab."""
        self.tab_handler.switch_to_new_tab()

    def close_new_tab_and_switch_back(self):
        """Close the new tab and switch back to the main window."""
        self.tab_handler.close_current_tab_and_switch_back()
