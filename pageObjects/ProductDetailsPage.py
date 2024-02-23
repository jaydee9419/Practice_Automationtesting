from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage():
    btn_addtobasket_xpath = "//button[normalize-space()='Add to basket']"
    lnk_description_xpath = "//a[normalize-space()='Description']"
    heading_description_xpath = "//h2[normalize-space()='Product Description']"
    txt_description_xpath = ("//div[@id='tab-description']//p[contains(text(),"
                             "'The Selenium WebDriver Recipes book is a quick pro')]")
    lnk_reviews_xpath = "//a[normalize-space()='Reviews (0)']"
    txt_reviews_xpath = "//h2[normalize-space()='Reviews']"
    lnk_viewbasket_xpath = "//a[normalize-space()='View Basket']"




    def __init__(self, driver):
        self.driver = driver

    def getAddtobasketbutton(self):
        try:
            basket_button = self.driver.find_element(By.XPATH, self.btn_addtobasket_xpath)
            basket_button.is_displayed()
            print(f"Text of button is: {basket_button.text}")

            return basket_button.text
        except:
            print("unable to find basket button element")

    def clickDiscription(self):
        self.driver.find_element(By.XPATH, self.lnk_description_xpath).click()

    def getHeaddingofDescription(self):
        heading = self.driver.find_element(By.XPATH, self.heading_description_xpath)
        print(heading.text)

    def getDetailDescriptionofProduct(self):
        detail_description = self.driver.find_element(By.XPATH, self.txt_description_xpath)
        print(detail_description.text)

    def clickReviewsButton(self):
        self.driver.find_element(By.XPATH, self.lnk_reviews_xpath).click()

    def getReviewsText(self):
        try:
            text = self.driver.find_element(By.XPATH, self.txt_reviews_xpath)
            print(text.text)
            return text.text
        except:
            print("Unable to locate text fields")

    def clickAddtobasketbutton(self):
        self.driver.find_element(By.XPATH, self.btn_addtobasket_xpath).click()

    def getViewBasket(self):
        try:
            view_basket = self.driver.find_element(By.XPATH, self.lnk_viewbasket_xpath)
            view_basket.is_displayed()
            print(f"Text of button is: {view_basket.text}")

            return view_basket.text
        except:
            print("unable to find View basket button element")

    def clickViewBasket(self):
        self.driver.find_element(By.XPATH, self.lnk_viewbasket_xpath).click()





