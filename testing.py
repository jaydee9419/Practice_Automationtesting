from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/shop/")
driver.maximize_window()
actions = ActionChains(driver)


element_left = driver.find_element(By.XPATH, "")
actions.drag_and_drop_by_offset(element_left, 85, 0).perform()

element_right = driver.find_element(By.XPATH, "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span[2]")
actions.drag_and_drop_by_offset(element_right, -58, 0).perform()


time.sleep(15)
driver.quit()

