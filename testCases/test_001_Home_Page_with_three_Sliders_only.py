from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.ShopPage import ShopPage
from pageObjects.HomePage import HomePage
import time

class Test_VerifySlides():
    baseURL = ReadConfig.getApplicationURL()

    def test_verifyslides(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickShop()

        self.sp = ShopPage(self.driver)
        self.sp.clickHome()

        self.hp = HomePage(self.driver)
        no_of_slides = self.hp.getSlides()
        if no_of_slides == 3:
            assert True
        else:
            assert False

        self.driver.quit()

