from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_to_element(driver, locator):
    try:
        # Wait for the element to be present and visible at the UI

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        # Scroll the page to the element using JavaScript
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        print("Scrolled to the element successfully.")
    except Exception as e:
        print(f"Failed to scroll to the element: {e}")
