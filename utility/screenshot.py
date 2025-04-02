import os
import time


def take_screenshot(driver, test_name):
    """Takes a screenshot and saves it with a timestamp in the 'screenshots' folder."""
    screenshots_dir = "screenshots"

    # Create the screenshots directory if it doesn't exist
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

    return screenshot_path  # Return the screenshot path
