import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def open_new_window(driver):
    """Opens a new browser window only if necessary."""
    if len(driver.window_handles) == 1:  # Ensure only one window is open before creating another
        print("Opening a new browser window...")
        driver.switch_to.new_window('window')



def get_driver(browser_name):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()

        # Check if geckodriver is installed
        geckodriver_path = shutil.which("geckodriver")
        if geckodriver_path:
            driver = webdriver.Firefox(service=FirefoxService(geckodriver_path), options=options)
        else:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Close initial empty window only if a second window exists
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[0])  # Switch to the first window
        driver.close()  # Close the empty window
        driver.switch_to.window(driver.window_handles[0])  # Switch back to the remaining window

    return driver
