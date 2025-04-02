from utility.config import URLS, USER_DATA
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.scroll import scroll_to_element

class WebPageActions:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        url_to_open = URLS.get(url)  # To open a certain URL from Config file
        self.driver.get(url_to_open)

    def click_element(self, locator):
        """Scroll and click an element"""
        scroll_to_element(self.driver, locator)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        """Enter text in a text field."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()  # Clear existing text before entering new text
        element.send_keys(text)

    def enter_text_from_config(self, locator, field_name):
        """Enter text into a field using data from config.py"""
        text_to_enter = USER_DATA.get(field_name, "")
        if text_to_enter:
            self.enter_text(locator, text_to_enter)
        else:
            raise ValueError(f"No valid text found for key: {field_name}")

    def get_element_value(self, locator):
        """Retrieve the current value of an input field"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")  # Get the current input value