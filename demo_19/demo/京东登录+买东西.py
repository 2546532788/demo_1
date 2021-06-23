from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
data = driver.window_handles
print(data)
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15235226482")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("124926ab")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(6)

driver.find_element_by_xpath("//*[@id='J_cate']/ul/li[2]/a[1]").click()
data1 = driver.window_handles
driver.switch_to.window(data1[1])
time.sleep(10)
driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div/div/div[2]/div/div/div/div[2]/div/div[1]/img').click()
data2 = driver.window_handles
driver.switch_to.window(data2[2])
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
# driver.find_element_by_xpath("")

time.sleep(3)
driver.quit()