import logging
import allure
from selenium import webdriver
from utility.browser_selection import get_driver, open_new_window
from utility.web_page_actions import WebPageActions
from utility.screenshot import take_screenshot

def before_all(context):
    """Set up global test configuration."""
    context.browser_name = context.config.userdata.get("browser", "chrome")
    context.multiwindow = context.config.userdata.get("multiwindow", "false").lower() == "true"

def before_scenario(context, scenario):
    """Initialize WebDriver before each scenario."""
    context.driver = get_driver(context.browser_name)

    if context.multiwindow and len(context.driver.window_handles) == 1:
        open_new_window(context.driver)

def after_scenario(context, scenario):
    """Take screenshot on failure and quit WebDriver after each scenario."""
    if scenario.status == "failed":
        screenshot_path = take_screenshot(context.driver, scenario.name)
        try:
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error(f"Error attaching screenshot to report: {e}")

    context.driver.quit()

def before_feature(context, feature):
    """Optional: Perform actions before a feature starts."""
    logging.info(f"Starting Feature: {feature.name}")

def after_feature(context, feature):
    """Optional: Perform actions after a feature ends."""
    logging.info(f"Finished Feature: {feature.name}")

def before_step(context, step):
    """Optional: Log the execution of each step."""
    logging.info(f"Executing Step: {step.name}")

def after_step(context, step):
    """Optional: Take screenshot on failed step."""
    if step.status == "failed":
        screenshot_path = take_screenshot(context.driver, step.name)
        try:
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="Step Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error(f"Could not attach screenshot: {e}")
