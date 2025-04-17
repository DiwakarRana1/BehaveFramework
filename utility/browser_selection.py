import shutil
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def open_new_window(driver):
    """Opens a new browser window only if necessary."""
    if len(driver.window_handles) == 1:
        print("Opening a new browser window...")
        driver.switch_to.new_window('window')

def get_driver(browser_name, use_healenium=False):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--headless=new")  # Uncomment for CI

        if use_healenium:
            print("Launching Chrome with Healenium proxy...")
            # options.add_argument('--proxy-server=http://172.17.0.1:8085')  # Adjust for Docker or local setup
            # options.add_argument('--ignore-certificate-errors')
            # options.add_argument('--disable-features=IsolateOrigins,site-per-process')

        # options = webdriver.ChromeOptions()

        driver = webdriver.Remote('http://localhost:8085/wd/hub', options=options)
        # driver = webdriver.Chrome(
        #     service=ChromeService(ChromeDriverManager().install()),
        #     options=options
        # )
        driver.maximize_window()

    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()

        if use_healenium:
            print("🔧 Launching Firefox with Healenium proxy...")
            options.set_preference("network.proxy.type", 1)
            options.set_preference("network.proxy.http", "localhost")
            options.set_preference("network.proxy.http_port", 8085)
            options.set_preference("network.proxy.ssl", "localhost")
            options.set_preference("network.proxy.ssl_port", 8085)

        geckodriver_path = shutil.which("geckodriver")
        if geckodriver_path:
            driver = webdriver.Firefox(
                service=FirefoxService(geckodriver_path),
                options=options
            )
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    return driver
