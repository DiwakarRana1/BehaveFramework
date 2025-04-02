# locators.py
from selenium.webdriver.common.by import By

class PageLocators:
    Elements = (By.XPATH, "//div[@class='category-cards']//*[text()='Elements']")
    textBox = (By.XPATH, "//div[@class='element-list collapse show']//*[text()='Text Box']")
    FullName = (By.XPATH, "//input[@id='userName']")
    Email = (By.ID, "userEmail")
    CurrentAddress = (By.ID, "currentAddress")
    PermanentAddress = (By.ID, "permanentAddress")
    SubmitButton = (By.ID, "submit")