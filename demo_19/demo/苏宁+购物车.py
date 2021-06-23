from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")
driver.maximize_window()
ac = ActionChains(driver)

driver.find_element_by_link_text("手机").click()
# driver.find_element_by_xpath()
data=driver.window_handles
print(data)
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='0000000000-945115237']/div/div/div[2]/div[2]/a").click()
data=driver.window_handles
print(data)
driver.switch_to.window(data[2])
driver.find_element_by_xpath("//*[@id='addCart']").click()
driver.find_element_by_xpath("/html/body/div[9]/div/div[2]/div/div[1]/a").click()
time.sleep(8)
driver.quit()