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
    NewTabButton = (By.XPATH, "//button[contains(text(), 'New Tab')]")
    AlertMenu = (By.XPATH, "//div[@class='header-text'][contains(text(), 'Alerts, Frame & Windows')]")
    BrowserMenu = (By.XPATH, "//span[@class='text'][contains(text(), 'Browser Windows')]")
    OutputName = (By.XPATH, "//p[@id='name']")
    OutputEmail = (By.XPATH, "//p[@id='email']")
    OutputCurrentAddress = (By.XPATH, "//p[@id='currentAddress']")
    OutputPermanentAddress = (By.XPATH, "//p[@id='permanentAddress']")