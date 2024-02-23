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
        self.cp.setCoupencode(ReadConfig.setCouponcode())
        self.cp.clickApplyCoupon()
        time.sleep(1)
        msg = self.cp.getInvalidCouponMsg()
        if msg == "The minimum spend for this coupon is ₹450.00.":
            assert True
        else:
            assert False

        self.cp.clickRemoveCart()
        time.sleep(1)
        confmsg = self.cp.getRemoveconfirmationMsg()
        if confmsg == "Thinking in HTML removed. Undo?":
            assert True
        else:
            assert False

        self.driver.quit()
