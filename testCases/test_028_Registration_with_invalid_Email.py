from pageObjects.BasePage import BasePage
from pageObjects.RegistraionAndSigninPage import RegistrationAndSigninPage
from utilities.readProperties import ReadConfig
import time

class Test_Registration():
    baseURL = ReadConfig.getApplicationURL()

    def test_registration(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickMyAccount()

        self.rp = RegistrationAndSigninPage(self.driver)
        self.rp.setRegmail("sfdfdsf")
        self.rp.setRegpassword(ReadConfig.setPassword())
        self.rp.clickRegButton()

        time.sleep(5)
        self.driver.quit()
