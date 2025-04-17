import allure
from selenium.webdriver.remote.webelement import WebElement
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
        print("URL:", url_to_open)
        if not url_to_open:
            raise ValueError(f"URL not found for key: {url}")
        self.driver.get(url_to_open)

    def find_element(self, locator):
        """Use driver.find_element to allow Healenium healing to work"""
        print(f"Finding element with locator: {locator}")  # Log the locator to debug
        try:
            element = self.driver.find_element(*locator)
            if element:
                print(f"Element found: {element}")  # Log successful find
            else:
                print(f"Element is None: {locator}")  # Log None element
            return element
        except Exception as e:
            print(
                f"Error finding element with locator: {locator}. Error: {str(e)}")  # Log error if element is not found
            raise

    # def _wait_for_element(self, locator, condition, action_desc="waiting for element"):
    #     """Reusable wait method with self-healing and clean error reporting"""
    #     try:
    #         element = WebDriverWait(self.driver, 20).until(
    #             lambda d: condition(self.find_element(locator))
    #         )
    #         if not element:
    #             raise ValueError(f"Element located, but it's None: {locator}")
    #         return element
    #     except TimeoutException as e:
    #         with allure.step(f"Element not found during: {action_desc}"):
    #             allure.attach(
    #                 str(locator),
    #                 name="Locator Info",
    #                 attachment_type=allure.attachment_type.TEXT
    #             )
    #         raise AssertionError(f"Failed to locate element for {action_desc}: {locator}") from e

    def _wait_for_element(self, locator, expected_condition, action_desc=""):
        try:
            by, value = locator
            print(f"Finding element with locator: {locator}")
            element = WebDriverWait(self.driver, 10).until(expected_condition((by, value)))
            print(f"Element found: {element}")
            return element
        except Exception as e:
            print(f"Failed to find element for {action_desc}: {locator}. Error: {str(e)}")
            raise

    def click_element(self, locator):
        """Scroll and click an element"""
        scroll_to_element(self.driver, locator)
        element = self._wait_for_element(
            locator,
            EC.element_to_be_clickable,
            action_desc="clicking element"
        )
        print(f"[DEBUG] Element returned: {element} | Type: {type(element)}")
        element.click()

    # def enter_text(self, locator, text):
    #     """Enter text in a text field."""
    #     try:
    #         element = self._wait_for_element(
    #             locator,
    #             EC.visibility_of_element_located,
    #             action_desc="entering text in element"
    #         )
    #
    #         if hasattr(element, "clear") and hasattr(element, "send_keys"):
    #
    #             element.clear()
    #             element.send_keys(text)
    #         else:
    #             raise ValueError(f"Element found but is not a WebElement: {locator}")
    #     except Exception as e:
    #         print(f"Error while entering text in element: {locator}. Error: {str(e)}")
    #         raise
    def enter_text(self, locator, text):
        """Enter text in a text field."""
        try:
            element = self._wait_for_element(
                locator,
                EC.visibility_of_element_located,
                action_desc="entering text in element"
            )

            print(f"[DEBUG] Element returned: {element} | Type: {type(element)}")
            element.clear()
            element.send_keys(text)

        except Exception as e:
            print(f"Error while entering text in element: {locator}. Error: {str(e)}")
            raise

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
