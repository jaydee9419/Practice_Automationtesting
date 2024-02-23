from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage():
    input_coupon_xpath = "//input[@id='coupon_code']"
    btn_couponapply_xpath = "//input[@name='apply_coupon']"
    txt_total_xpath = "//strong//span[@class='woocommerce-Price-amount amount']"
    txt_invalidcoupon_xpath = "//div[@id='body']//li[1]"
    lnk_removecartitem_xpath = "//a[normalize-space()='×'][1]"
    txt_removalConfmsg_xpath = "//div[@class='woocommerce-message']"
    input_quantity_xpath = "//input[@title='Qty']"
    btn_updatecart_xpath = "//input[@name='update_cart']"



    def __init__(self, driver):
        self.driver = driver

    def setCoupencode(self, coupon):
        self.driver.find_element(By.XPATH, self.input_coupon_xpath).send_keys(coupon)

    def clickApplyCoupon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_couponapply_xpath))).click()

    def getTotalAmount(self):
        try:
            total = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_total_xpath)))
            print(f"Final Price of the product after Discount: {total.text}")
            return total.text
        except:
            print("Unable to find the price element")

    def getInvalidCouponMsg(self):
        try:
            msg = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_invalidcoupon_xpath)))
            print(f"Error message: {msg.text}")
            return msg.text
        except:
            print("Unable to find the invalid msg element")

    def clickRemoveCart(self):
        self.driver.find_element(By.XPATH, self.lnk_removecartitem_xpath).click()

    def getRemoveconfirmationMsg(self):
        try:
            msg = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_removalConfmsg_xpath)))
            print(f"Error message: {msg.text}")
            return msg.text
        except:
            print("Unable to find the removed cart msg element")

    def getQuntityInfo(self):
        try:
            quantity = self.driver.find_element(By.XPATH, self.input_quantity_xpath)
            print(f"No of quantity in cart: {quantity.text}")
            return quantity.text
        except:
            print("Unable to get quantity info")

    def clearQuntity(self):
        self.driver.find_element(By.XPATH, self.input_quantity_xpath).clear()

    def increaseQuntity(self):
        self.driver.find_element(By.XPATH, self.input_quantity_xpath).send_keys('10')

    def decreaseQuantity(self):
        self.driver.find_element(By.XPATH, self.input_quantity_xpath).send_keys("2")

    def clickUpdatecart(self):
        self.driver.find_element(By.XPATH, self.btn_updatecart_xpath).click()





