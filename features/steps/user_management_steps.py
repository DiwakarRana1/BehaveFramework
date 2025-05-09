from behave import given, when, then
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.user_management import UserManagement


@given("I am on the User Management Home Page")
def open_usm_home_page(context):
    context.usm_home_page = UserManagement(context.driver)
    context.usm_home_page.open("userManagement")

@when("I Click on Login Button")
def click_on_login(context):
    context.usm_home_page.click_on_usm_login_button()

@when("I Enter Credentials")
def enter_username_password(context):
    """Enter Credentials and Click on Login Button"""
    context.usm_home_page.enter_usm_credentials()
    context.usm_home_page.click_on_usm_submit_button()
    # Add a wait to allow the page to redirect
    time.sleep(3)
    print(f"Current URL after login attempt: {context.driver.current_url}")


@then("I should see the Dashboard")
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