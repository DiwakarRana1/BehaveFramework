from behave import given, when, then

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

@then("I should see the Admin Page")
def verify_logged_in(context):
    """Assertion for Successful Login"""
    assert "dashboard" in context.driver.current_url, "URL does not contain 'dashboard'"