from selenium.webdriver.common.by import By


class BasePage():
    lnk_shop_xpath = "//a[normalize-space()='Shop']"
    lnk_MyAccount_xpath = "//a[normalize-space()='My Account']"
    lnk_testcases_xpath = "//a[normalize-space()='Test Cases']"
    lnk_ATSite_xpath = "//a[normalize-space()='AT Site']"
    lnk_DemoSite_xpath = "//a[normalize-space()='Demo Site']"

    def __init__(self, driver):
        self.driver = driver

    def clickShop(self):
        self.driver.find_element(By.XPATH, self.lnk_shop_xpath).click()

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_MyAccount_xpath).click()

    def clickTestCases(self):
        self.driver.find_element(By.XPATH, self.lnk_testcases_xpath).click()

    def clickATSite(self):
        self.driver.find_element(By.XPATH, self.lnk_ATSite_xpath).click()

    def clickDemoSite(self):
        self.driver.find_element(By.XPATH, self.lnk_DemoSite_xpath).click()
