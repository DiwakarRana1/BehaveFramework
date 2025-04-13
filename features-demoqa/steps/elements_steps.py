from behave import given, when, then
from pages.elements_page import ElementsPage

@given("I am on the DEMOQA Home Page")
def step_open_demoqa(context):
    """Navigates to the DemoQA homepage using the configured URL key."""
    context.elements_page = ElementsPage(context.driver)
    context.elements_page.open("demoQa")

@when("I click on the Elements Section")
def step_click_elements(context):
    """Clicks on the 'Elements' section."""
    context.elements_page.click_elements_box()

@then("I should see the Elements Page")
def step_verify_elements_page(context):
    """Verifies that the Elements page is displayed."""
    assert "elements" in context.driver.current_url, "URL does not contain 'elements'"