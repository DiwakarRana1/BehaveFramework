import logging
import os

import allure
from utility.browser_selection import get_driver, open_new_window
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
    """Take a screenshot on scenario failure and attach it to Allure."""
    if scenario.status == "failed":
        screenshot_path = take_screenshot(context.driver, scenario.name)
        if os.path.exists(screenshot_path):  # Ensure screenshot exists before attaching
            try:
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(image_file.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
                logging.info(f"Failure screenshot attached for scenario: {scenario.name}")
            except Exception as e:
                logging.error(f"Error attaching failure screenshot: {e}")
        else:
            logging.error(f"Failure screenshot not found for scenario: {scenario.name}")

    context.driver.quit()


def before_feature(context, feature):
    """Optional: Perform actions before a feature starts."""
    logging.info(f"Starting Feature: {feature.name}")

def after_feature(context, feature):
    """Optional: Perform actions after a feature ends."""
    logging.info(f"Finished Feature: {feature.name}")

def before_step(context, step):
    """Log the execution of each step."""
    logging.info(f"Executing Step: {step.name}")

def after_step(context, step):
    """Take a screenshot after every step and attach it to the Allure report."""
    screenshot_path = take_screenshot(context.driver, step.name)  # Take screenshot for every step
    if os.path.exists(screenshot_path):  # Ensure screenshot is saved before attaching
        try:
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=f"Step Screenshot - {step.name}", attachment_type=allure.attachment_type.PNG)
            logging.info(f"Screenshot attached for step: {step.name}")
        except Exception as e:
            logging.error(f"Could not attach screenshot for step {step.name}: {e}")
    else:
        logging.error(f"Screenshot not found for step: {step.name}")
