from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.ShopPage import ShopPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailsPage import ProductDetailsPage
from pageObjects.CkeckoutPage import CheckoutPage
import time

class Test_CouponApply():
    baseURL = ReadConfig.getApplicationURL()

    def test_couponapply(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickShop()

        self.sp = ShopPage(self.driver)
        self.sp.clickHome()

        self.hp = HomePage(self.driver)
        self.hp.clickThinking_in_HTMLProduct()

        self.pdp = ProductDetailsPage(self.driver)
        self.pdp.clickAddtobasketbutton()
        self.pdp.clickViewBasket()

        self.cp = CheckoutPage(self.driver)
        self.cp.getQuntityInfo()
        time.sleep(1)

        self.cp.clearQuntity()
        time.sleep(1)
        self.cp.increaseQuntity()
        self.cp.clickUpdatecart()
        time.sleep(1)
        self.cp.getQuntityInfo()

        time.sleep(1)
        self.cp.clearQuntity()
        time.sleep(1)
        self.cp.decreaseQuantity()
        self.cp.clickUpdatecart()
        time.sleep(1)
        self.cp.getQuntityInfo()
        time.sleep(5)

        self.driver.quit()


