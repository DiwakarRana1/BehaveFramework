import logging
import os
import time
from datetime import datetime

import allure
from utility.browser_selection import get_driver, open_new_window
from utility.screenshot import take_screenshot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def before_all(context):
    """Set up global test configuration."""
    context.browser_name = context.config.userdata.get("browser", "chrome")
    context.multiwindow = context.config.userdata.get("multiwindow", "false").lower() == "true"
    context.use_healenium = context.config.userdata.get("healenium", "false").lower() == "true"
    
    logger.info(f"Test Configuration:")
    logger.info(f"Browser: {context.browser_name}")
    logger.info(f"Multi-window: {context.multiwindow}")
    logger.info(f"Healenium: {context.use_healenium}")

def before_scenario(context, scenario):
    """Initialize WebDriver before each scenario."""
    logger.info(f"Starting scenario: {scenario.name}")
    try:
        context.driver = get_driver(context.browser_name, use_healenium=context.use_healenium)
        if context.multiwindow and len(context.driver.window_handles) == 1:
            open_new_window(context.driver)
        logger.info(f"WebDriver initialized successfully for scenario: {scenario.name}")
    except Exception as e:
        logger.error(f"Failed to initialize WebDriver for scenario {scenario.name}: {str(e)}")
        raise

def after_scenario(context, scenario):
    """Take a screenshot on scenario failure and attach it to Allure."""
    try:
        if scenario.status == "failed":
            logger.error(f"Scenario failed: {scenario.name}")
            screenshot_path = take_screenshot(context.driver, f"{scenario.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            
            if os.path.exists(screenshot_path):
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"Failure Screenshot - {scenario.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                logger.info(f"Failure screenshot attached for scenario: {scenario.name}")
            else:
                logger.error(f"Failure screenshot not found for scenario: {scenario.name}")
    except Exception as e:
        logger.error(f"Error in after_scenario for {scenario.name}: {str(e)}")
    finally:
        try:
            context.driver.quit()
            logger.info(f"WebDriver closed for scenario: {scenario.name}")
        except Exception as e:
            logger.error(f"Error closing WebDriver for scenario {scenario.name}: {str(e)}")

def before_feature(context, feature):
    """Perform actions before a feature starts."""
    logger.info(f"Starting Feature: {feature.name}")
    logger.info(f"Feature Description: {feature.description}")
    logger.info(f"Feature Tags: {feature.tags}")

def after_feature(context, feature):
    """Perform actions after a feature ends."""
    logger.info(f"Finished Feature: {feature.name}")
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
            logger.info("WebDriver closed after feature completion")
        except Exception as e:
            logger.error(f"Error closing WebDriver after feature: {str(e)}")

def before_step(context, step):
    """Log the execution of each step."""
    logger.info(f"Executing Step: {step.name}")
    context.step_start_time = time.time()

def after_step(context, step):
    """Take a screenshot after every step and attach it to the Allure report."""
    try:
        step_duration = time.time() - context.step_start_time
        logger.info(f"Step completed: {step.name} (Duration: {step_duration:.2f}s)")
        
        screenshot_path = take_screenshot(
            context.driver,
            f"{step.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        
        if os.path.exists(screenshot_path):
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=f"Step Screenshot - {step.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            logger.info(f"Screenshot attached for step: {step.name}")
        else:
            logger.error(f"Screenshot not found for step: {step.name}")
            
        if step.status == "failed":
            logger.error(f"Step failed: {step.name}")
            if hasattr(step, 'error_message'):
                logger.error(f"Error message: {step.error_message}")
    except Exception as e:
        logger.error(f"Error in after_step for {step.name}: {str(e)}")
