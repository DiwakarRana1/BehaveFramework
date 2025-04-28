import logging
from selenium import webdriver
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def open_new_window(driver):
    """Opens a new browser window only if necessary."""
    if len(driver.window_handles) == 1:
        logger.info("Opening a new browser window...")
        driver.switch_to.new_window('window')

def get_healenium_capabilities(browser_name):
    """Returns Healenium capabilities based on browser type."""
    base_capabilities = {
        "healenium:enable": True,
        "healenium:serverHost": "healenium",
        "healenium:serverPort": 7878,
        "healenium:imitatePort": 8000,
        "healenium:recording": True,
        "healenium:reportScreenshots": True,
        "healenium:reportHealingResults": True,
        "healenium:healEnabled": True,
        "healenium:recoveryTries": 5,
        "healenium:scoreCap": 0.6,
        "healenium:imitate": True,
        "healenium:findElementsAutoHealing": True,
        "healenium:pageSourceCapture": True,
        "healenium:timezone": "Asia/Kolkata"
    }
    
    if browser_name.lower() == "chrome":
        base_capabilities["browserName"] = "chrome"
    elif browser_name.lower() == "firefox":
        base_capabilities["browserName"] = "firefox"
    
    return base_capabilities

def get_driver(browser_name, use_healenium=False):
    """
    Initialize and return a WebDriver instance.
    
    Args:
        browser_name (str): Name of the browser to use (chrome/firefox)
        use_healenium (bool): Whether to use Healenium for element healing
    
    Returns:
        WebDriver: Configured WebDriver instance
    """
    try:
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-software-rasterizer")
            options.add_argument("--headless")
            
            # Set the Chrome binary location
            chrome_paths = [
                "/usr/bin/google-chrome-stable",
                "/usr/bin/google-chrome",
                "/usr/bin/chromium-browser"
            ]
            for path in chrome_paths:
                if os.path.exists(path):
                    options.binary_location = path
                    break
            
            if use_healenium:
                logger.info("Launching Chrome with Healenium...")
                capabilities = get_healenium_capabilities(browser_name)
                options.set_capability('browserName', 'chrome')
                for key, value in capabilities.items():
                    options.set_capability(key, value)
                driver = webdriver.Remote(
                    command_executor='http://localhost:8085',
                    options=options
                )
            else:
                logger.info("Launching regular Chrome...")
                try:
                    # Let Selenium Manager handle the driver version
                    from selenium.webdriver.chrome.service import Service
                    from selenium.webdriver.chrome.service import Service as ChromeService
                    from webdriver_manager.chrome import ChromeDriverManager
                    
                    service = ChromeService(ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=options)
                except Exception as e:
                    logger.error(f"Failed to initialize Chrome driver: {str(e)}")
                    raise
                
            driver.maximize_window()
            return driver
            
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            
            if use_healenium:
                logger.info("Launching Firefox with Healenium...")
                capabilities = get_healenium_capabilities(browser_name)
                options.set_capability('browserName', 'firefox')
                for key, value in capabilities.items():
                    options.set_capability(key, value)
                driver = webdriver.Remote(
                    command_executor='http://localhost:8085',
                    options=options
                )
            else:
                logger.info("Launching regular Firefox...")
                driver = webdriver.Firefox(options=options)
                
            driver.maximize_window()
            return driver
            
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    except Exception as e:
        logger.error(f"Failed to initialize {browser_name} driver: {str(e)}")
        raise

