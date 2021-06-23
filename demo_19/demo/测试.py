from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

ac = ActionChains(driver)

driver.find_element_by_link_text("手机").click()

time.sleep(10)

driver.quit()
