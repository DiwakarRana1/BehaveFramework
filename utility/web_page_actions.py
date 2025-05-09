import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utility.config import URLS, USER_DATA, HRM_DATA, USER_MGT
from utility.scroll import scroll_to_element
from utility.fake_data import get_latest_employee
import time
import logging


class WebPageActions:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open(self, url):
        """Open a URL from config"""
        url_to_open = URLS.get(url)
        self.logger.info(f"Opening URL: {url_to_open}")
        if not url_to_open:
            raise ValueError(f"URL not found for key: {url}")
        self.driver.get(url_to_open)
        time.sleep(2)  # Small delay to ensure page is loaded

    def find_element(self, locator):
        """Find element with locator fallback + single Healenium healing attempt on the final locator"""
        try:
            self.logger.info(f"Finding element with locator(s): {locator}")

            # Normalize locators to a list
            if not isinstance(locator, (list, tuple)) or isinstance(locator[0], str):
                locators = [locator]
            else:
                locators = locator

            # Try each locator quickly
            for i, loc in enumerate(locators):
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(loc)
                    )
                    self.logger.info(f"Element found using locator: {loc}")
                    return element
                except TimeoutException:
                    self.logger.info(f"Locator {loc} failed in initial attempt.")
                    continue  # Try the next one

            # If none worked, try healing ONLY on the last locator
            final_locator = locators[-1]
            self.logger.info(f"Attempting healing on final locator: {final_locator}")
            try:
                element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(final_locator)
                )
                self.logger.info(f"Element found after healing using locator: {final_locator}")
                return element
            except TimeoutException:
                self.logger.error(f"Healing failed for final locator: {final_locator}")
                raise NoSuchElementException(f"Element not found with any locator, healing also failed on: {final_locator}")

        except Exception as e:
            self.logger.error(f"Final failure in locating element(s): {locator}. Error: {e}")
            screenshot_path = "healing_failure.png"
            self.driver.save_screenshot(screenshot_path)
            with allure.step("Element not found"):
                allure.attach.file(
                    screenshot_path,
                    name="Healing Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    str(locator),
                    name="Failed Locator(s)",
                    attachment_type=allure.attachment_type.TEXT
                )
            raise


    def _wait_for_element(self, locator, expected_condition, action_desc=""):
        """Enhanced wait method with improved Healenium healing support"""
        try:
            self.logger.info(f"Waiting for element: {locator} with condition: {expected_condition.__name__}")
            # First attempt with shorter timeout
            element = WebDriverWait(self.driver, 10).until(
                expected_condition(locator)
            )
            self.logger.info(f"Element found on first attempt for {action_desc}")
            return element
        except TimeoutException:
            self.logger.info(f"Initial attempt failed for {action_desc}, waiting for healing...")
            try:
                # Second attempt with longer timeout for healing
                element = WebDriverWait(self.driver, 30).until(
                    expected_condition(locator)
                )
                self.logger.info(f"Element found after healing for {action_desc}")
                return element
            except TimeoutException as e:
                self.logger.error(f"Element not found even after healing: {locator}")
                # Capture screenshot and page source for debugging
                screenshot_path = f"healing_failure_{action_desc.replace(' ', '_')}.png"
                self.driver.save_screenshot(screenshot_path)
                with allure.step(f"Element not found during: {action_desc}"):
                    allure.attach.file(
                        screenshot_path,
                        name=f"Healing Failure Screenshot - {action_desc}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    allure.attach(
                        self.driver.page_source,
                        name="Page Source",
                        attachment_type=allure.attachment_type.HTML
                    )
                    allure.attach(
                        str(locator),
                        name="Failed Locator",
                        attachment_type=allure.attachment_type.TEXT
                    )
                raise AssertionError(f"Failed to locate element for {action_desc}: {locator}") from e

    def click_element(self, locator):
        """Click element with healing support"""
        scroll_to_element(self.driver, locator)
        element = self._wait_for_element(
            locator,
            EC.element_to_be_clickable,
            action_desc="clicking element"
        )
        self.logger.info(f"Clicking element: {locator}")
        element.click()

    def enter_text(self, locator, text):
        """Enter text in a text field with enhanced healing capabilities."""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.error(f"Error entering text '{text}' in element: {locator}. Error: {str(e)}")
            raise

    def enter_text_from_config(self, locator, field_name):
        """Enter text from config with healing support"""
        text = USER_DATA.get(field_name) or HRM_DATA.get(field_name) or USER_MGT.get(field_name)
        if not text:
            raise ValueError(f"Text not found for field: {field_name}")
        self.enter_text(locator, text)

    def get_element_value(self, locator):
        """Get element value with healing support"""
        element = self._wait_for_element(
            locator,
            EC.presence_of_element_located,
            action_desc="getting element value"
        )
        return element.get_attribute("value")

    @property
    def latest_fake_employee(self):
        """Get latest fake employee data"""
        return get_latest_employee()
