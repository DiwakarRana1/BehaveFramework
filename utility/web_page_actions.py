import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utility.config import URLS, USER_DATA, HRM_DATA
from utility.scroll import scroll_to_element
from utility.fake_data import get_latest_employee  # ✅ Import this

class WebPageActions:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Open a URL from config"""
        url_to_open = URLS.get(url)
        if not url_to_open:
            raise ValueError(f"URL not found for key: {url}")
        self.driver.get(url_to_open)

    def _wait_for_element(self, locator, condition, action_desc="waiting for element"):
        """Reusable wait method with clean error reporting"""
        try:
            return WebDriverWait(self.driver, 10).until(condition(locator))
        except TimeoutException as e:
            with allure.step(f"Element not found during: {action_desc}"):
                allure.attach(
                    str(locator),
                    name="Locator Info",
                    attachment_type=allure.attachment_type.TEXT
                )
            raise AssertionError(f"Failed to locate element for {action_desc}: {locator}") from e

    def click_element(self, locator):
        """Scroll and click an element"""
        scroll_to_element(self.driver, locator)
        element = self._wait_for_element(
            locator,
            EC.element_to_be_clickable,
            action_desc="clicking element"
        )
        element.click()

    def enter_text(self, locator, text):
        """Enter text in a text field."""
        element = self._wait_for_element(
            locator,
            EC.visibility_of_element_located,
            action_desc="entering text in element"
        )
        element.clear()
        element.send_keys(text)

    def enter_text_from_config(self, locator, field_name):
        """Enter text into a field using data from config.py"""
        # text_to_enter = USER_DATA.get(field_name, "")
        text_to_enter = HRM_DATA.get(field_name, "")
        if text_to_enter:
            self.enter_text(locator, text_to_enter)
        else:
            raise ValueError(f"No valid text found for key: {field_name}")

    def get_element_value(self, locator):
        """Retrieve the current value of an input field"""
        element = self._wait_for_element(
            locator,
            EC.visibility_of_element_located,
            action_desc="getting value from element"
        )
        return element.get_attribute("value")

    @property
    def latest_fake_employee(self):
        """Return the most recently created fake employee"""
        return get_latest_employee()
