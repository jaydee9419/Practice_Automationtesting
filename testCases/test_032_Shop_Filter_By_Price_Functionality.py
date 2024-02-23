from pageObjects.ShopPage import ShopPage
from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
import time


class Test_Filter():
    baseURL = ReadConfig.getApplicationURL()

    def test_filter(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickShop()

        self.sp = ShopPage(self.driver)
        self.sp.dragLeftToRight()
        self.sp.dragRightToLeft()
        self.sp.clickFilter()
        time.sleep(2)
        self.sp.books()
        self.sp.bookNames()
        for item in self.sp.bookNames():
            print(item.text)

        time.sleep(5)
        self.driver.quit()
