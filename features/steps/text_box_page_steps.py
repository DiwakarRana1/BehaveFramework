from behave import when, then
from pages.text_box_page import TextBoxPage
from utility.config import USER_DATA

@when('I click on the "Text Box" menu')
def step_click_text_box(context):
    context.text_box_page = TextBoxPage(context.driver)
    context.text_box_page.click_on_text_box()

@when("I enter text in all fields")
def step_fill_text_fields(context):
    context.text_box_page.fill_text_fields()

@when("I click on the submit button")
def step_submit_form(context):
    context.text_box_page.submit_button_click()

@then("the input values should be correctly displayed")
def step_verify_input_values(context):
    assert context.text_box_page.get_element_value(context.text_box_page.full_name_locator) == USER_DATA["Full Name"], "Full Name Mismatch!"
