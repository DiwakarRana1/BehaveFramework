from behave import when, then
from pages.alerts_frame_windows import NewTabPage

@when("I click on the Alerts, Frames & Windows")
def step_click_alerts_menu(context):
    """Click on the Alerts, Frames & Windows menu."""
    new_tab_page = NewTabPage(context.driver)
    new_tab_page.click_on_alert_menu()

@when("I click on Browser Windows")
def step_click_browser_menu(context):
    """Click on the Browser Windows option."""
    new_tab_page = NewTabPage(context.driver)
    new_tab_page.click_on_browser_menu()

@when("I click on the new tab button")
def step_click_new_tab_button(context):
    """Click on the button to open a new tab."""
    new_tab_page = NewTabPage(context.driver)
    new_tab_page.click_on_new_tab_button()

@then("the switching of tabs will done")
def step_switch_to_new_tab(context):
    """Switch to the newly opened tab and then switch back."""
    new_tab_page = NewTabPage(context.driver)
    new_tab_page.switch_to_new_tab()  # Switch to the new tab
    new_tab_page.close_new_tab_and_switch_back()
