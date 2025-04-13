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
    HrmUsername = (By.XPATH, "//input[@placeholder= 'Username']")
    HrmPassword = (By.XPATH, "//input[@placeholder= 'Password']")
    HrmSubmit = (By.XPATH, "//button[@type='submit']")
    HrmAdmin = (By.XPATH, "//span[text()= 'Admin']")
    HrmPIM = (By.XPATH, "//span[text()= 'PIM']")
    AddButton= (By.XPATH, "//button[normalize-space()='Add']")
    HrmFirstName= (By.XPATH, "//input[@placeholder='First Name']")
    HrmLastName= (By.XPATH, "//input[@placeholder='Last Name']")
    SaveButton= (By.XPATH, "//button[normalize-space()='Save']")
    EmpId = (By.XPATH, "//input[@placeholder='Last Name']/following::input[1]")
    PimEmpId = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    SearchButton = (By.XPATH, "//button[normalize-space()='Search']")
    DeleteButton = (By.XPATH, "//div[normalize-space()='Actions']/following::button[@type='button'][2]")
    ConfirmDelete = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
