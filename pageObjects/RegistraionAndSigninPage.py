from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class RegistrationAndSigninPage():
    input_regmail_xpath = "//input[@id='reg_email']"
    input_regpassword_xpath = "//input[@id='reg_password']"
    btn_registration_xpath = "//input[@name='register']"
    text_dashboard_xpath = "//a[normalize-space()='Dashboard']"

    input_loginmail_xpath = "//input[@id='username']"
    input_loginpassword_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@name='login']"

    def __init__(self, driver):
        self.driver = driver

    def setRegmail(self, email):
        self.driver.find_element(By.XPATH, self.input_regmail_xpath).send_keys(email)

    def setRegpassword(self, pwd):
        self.driver.find_element(By.XPATH, self.input_regpassword_xpath).send_keys(pwd)

    def clickRegButton(self):
        self.driver.find_element(By.XPATH, self.btn_registration_xpath).click()

    def getConfMsg(self):
        msg = self.driver.find_element(By.XPATH, self.text_dashboard_xpath)
        print(msg.text)




