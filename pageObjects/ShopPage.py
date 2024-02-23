from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class ShopPage():
    lnk_home_xpath = "//a[normalize-space()='Home']"
    drag_left_xpath = "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span[1]"
    drag_right_xpath = "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span[2]"
    btn_filter_xpath = "//button[normalize-space()='Filter']"
    lst_books_xpath = "//li//a //img"
    names_books_xpath = "//h3"
    sort_books_xpath = "//option[@value='rating']"

    def __init__(self, driver):
        self.driver = driver



    def clickHome(self):
        self.driver.find_element(By.XPATH, self.lnk_home_xpath).click()

    def dragLeftToRight(self):
        left_dot = self.driver.find_element(By.XPATH, self.drag_left_xpath)
        actions = ActionChains(self.driver)

        actions.drag_and_drop_by_offset(left_dot, 85, 0).perform()

    def dragRightToLeft(self):
        right_dot = self.driver.find_element(By.XPATH, self.drag_right_xpath)
        actions = ActionChains(self.driver)

        actions.drag_and_drop_by_offset(right_dot, 0, 0).perform()

    def clickFilter(self):
        self.driver.find_element(By.XPATH, self.btn_filter_xpath).click()


    def books(self):
        no_of_books = self.driver.find_elements(By.XPATH, self.lst_books_xpath)
        print(len(no_of_books))

    def bookNames(self):
        names = self.driver.find_elements(By.XPATH, self.names_books_xpath)
        return names

    def sorting_books(self):
        self.driver.find_element(By.XPATH, self.sort_books_xpath).click()
