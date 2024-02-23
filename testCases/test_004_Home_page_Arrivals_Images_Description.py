from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.ShopPage import ShopPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailsPage import ProductDetailsPage
import time

class Test_VerifyProductNavigation():
    baseURL = ReadConfig.getApplicationURL()

    def test_verifyproductnavigation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickShop()

        self.sp = ShopPage(self.driver)
        self.sp.clickHome()

        self.hp = HomePage(self.driver)
        self.hp.clickProduct()

        self.pdp = ProductDetailsPage(self.driver)
        self.pdp.clickDiscription()
        self.pdp.getHeaddingofDescription()
        self.pdp.getDetailDescriptionofProduct()



        self.driver.quit()
