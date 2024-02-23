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
        self.hp.clickProduct()

        self.pdp = ProductDetailsPage(self.driver)
        self.pdp.clickAddtobasketbutton()
        self.pdp.clickViewBasket()

        self.cp = CheckoutPage(self.driver)
        self.cp.setCoupencode(ReadConfig.setCouponcode())
        self.cp.clickApplyCoupon()
        time.sleep(1)
        total = self.cp.getTotalAmount()
        if total == "₹459.00" or "₹510.00":
            assert True
        else:
            assert False

        self.driver.quit()
