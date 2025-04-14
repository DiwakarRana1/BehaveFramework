import time

from behave import when
from pages.employee_page import EmployeePage
from utility.fake_data import generate_employee_data




@when("I navigate to the Add Employee page")
def step_navigate_to_add_employee(context):
    context.employee_page = EmployeePage(context.driver)
    context.employee_page.click_on_pim()
    context.employee_page.click_on_add()


@when("I fill in new employee details")
def step_fill_employee_details(context):
    employee = generate_employee_data()
    context.employee_data = employee  # Save for later validation
    context.employee_page.enter_emp_details(employee)


@when("I save the employee")
def step_save_employee(context):
    context.employee_page.click_on_save()


@when("I click on PIM")
def back_on_pim(context):
    context.employee_page.click_on_pim()

@when("Search the EmpID")
def enter_emp_id(context):
    context.employee_page.enter_emp_id()
    context.employee_page.click_on_search()

@when("Delete the Employee")
def delete_emp(context):
    context.employee_page.click_on_delete()
    time.sleep(1)







