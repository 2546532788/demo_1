from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://8.129.91.152:8765/")
driver.maximize_window()

driver.find_element_by_link_text("免费注册").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("13434239099")
time.sleep(20)
driver.find_element_by_link_text("获取短信验证码").click()
time.sleep(1)
a=driver.find_element_by_class_name("layui-layer-content").text
b = a.split("验证码为")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/input").send_keys(b[-1])
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("123456AB")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
time.sleep(2)
driver.find_element_by_link_text("系统自动分配").click()
time.sleep(10)
driver.quit()



