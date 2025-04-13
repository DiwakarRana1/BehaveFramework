from selenium.webdriver import Keys

from utility.fake_data import get_latest_employee
from utility.locators import PageLocators
from utility.web_page_actions import WebPageActions
import time


class EmployeePage(WebPageActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.pim_locator = PageLocators.HrmPIM
        self.emp_first_name = PageLocators.HrmFirstName
        self.emp_last_name = PageLocators.HrmLastName
        self.save_button = PageLocators.SaveButton
        self.add_button = PageLocators.AddButton
        self.emp_id = PageLocators.EmpId
        self.pim_emp_id = PageLocators.PimEmpId
        self.search_button = PageLocators.SearchButton
        self.delete_button = PageLocators.DeleteButton
        self.confirm_delete = PageLocators.ConfirmDelete

    def click_on_pim(self):
        self.click_element(self.pim_locator)

    def click_on_add(self):
        self.click_element(self.add_button)

    def enter_emp_details(self, employee):
        self.enter_text(self.emp_first_name, employee["first_name"])
        self.enter_text(self.emp_last_name, employee["last_name"])

        emp_id_field = self.driver.find_element(*self.emp_id)
        emp_id_field.click()
        emp_id_field.send_keys(Keys.CONTROL + "a")
        emp_id_field.send_keys(Keys.DELETE)
        time.sleep(0.5)
        emp_id_field.send_keys(str(employee["employee_id"]))

    def click_on_save(self):
        self.click_element(self.save_button)

    def enter_emp_id(self):
        employee = get_latest_employee()
        emp_id = str(employee["employee_id"])
        self.enter_text(self.pim_emp_id, emp_id)

    def click_on_search(self):
        self.click_element(self.search_button)

    def click_on_delete(self):
        time.sleep(0.3)
        self.click_element(self.delete_button)
        time.sleep(0.5)
        self.click_element(self.confirm_delete)