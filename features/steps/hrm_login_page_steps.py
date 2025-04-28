from behave import given, when, then
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.hrm_login_page import HrmLoginPage


@given ("I am on the HRM Login Page")
def open_hrm_login_page(context):
    context.hrm_login_page = HrmLoginPage(context.driver)
    context.hrm_login_page.open("hrmDemo")

@when ("I Enter User Credentials")
def enter_username_password(context):
    """Enter Credentials and Click on Login Button"""
    context.hrm_login_page.enter_credentials()
    context.hrm_login_page.click_on_login_button()
    # Add a wait to allow the page to redirect
    time.sleep(3)
    print(f"Current URL after login attempt: {context.driver.current_url}")


@then("I should see the Admin Page")
def verify_logged_in(context):
    """Assertion for Successful Login"""
    print(f"Final URL: {context.driver.current_url}")
    print(f"Page title: {context.driver.title}")
    print(f"Page source contains 'dashboard': {'dashboard' in context.driver.page_source}")
    
    # Try to wait for dashboard to appear in URL
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: "dashboard" in driver.current_url
        )
    except TimeoutException:
        print("Timeout waiting for dashboard URL")
    
    assert "dashboard" in context.driver.current_url, "URL does not contain 'dashboard'"