from selenium.webdriver.common.by import By


class HomePage():
    lnk_slides_xpath = "//*[@id='n2-ss-6']//div//div//div//div//div//img"
    lnk_arivals_xpath = "//div//h3"
    img_Selenium_Ruby_xpath = "//img[@title='Selenium Ruby']"
    img_Thinking_in_HTML_xpath = "//img[@title='Thinking in HTML']"

    def __init__(self, driver):
        self.driver = driver

    def getSlides(self):
        try:
            slides = self.driver.find_elements(By.XPATH, self.lnk_slides_xpath)
            count = len(slides)
            print(f"No of slides in home page: {count}")
            return len(slides)
        except:
            print("Unable to find the slides element")

    def getArrivals(self):
        try:
            arrivals = self.driver.find_elements(By.XPATH, self.lnk_arivals_xpath)
            count = len(arrivals)
            print(f"No of new Arrivals: {count}")
            for item in arrivals:
                print(item.text)
            return len(arrivals)
        except:
            print("Unable to find the arrivals element")

    def clickSeleniumRubyProduct(self):
        self.driver.find_element(By.XPATH, self.img_Selenium_Ruby_xpath).click()

    def clickThinking_in_HTMLProduct(self):
        self.driver.find_element(By.XPATH, self.img_Thinking_in_HTML_xpath).click()
