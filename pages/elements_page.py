from utility.web_page_actions import WebPageActions
from utility.locators import PageLocators

class ElementsPage(WebPageActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.elements_box_locator = PageLocators.Elements

    def click_elements_box(self):
        """Clicks on the Elements section"""
        self.click_element(self.elements_box_locator)
