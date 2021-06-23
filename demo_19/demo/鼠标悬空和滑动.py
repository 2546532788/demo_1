from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

derver=webdriver.Chrome()

# derver.get("https://www.jd.com/")
# derver.maximize_window()
# # 创建actionchains：事件管理对象
# ac = ActionChains(derver)
# # 搜索我的京东元素
# # derver.find_element_by_link_text("//*[@id='nc_1__scale_text']/span").click()
# ele=derver.find_element_by_xpath("//*[@id='ttbar-myjd']/div[1]/a")
# # 悬停到这个元素
# ac.move_to_element(ele).perform()
derver.get("https://www.qcc.com/")
derver.maximize_window()

ac = ActionChains(derver)

derver.find_element_by_link_text("登录 | 注册").click()
time.sleep(6)
# 确定滑块
ele = derver.find_element_by_xpath("//*[@id='nc_1_n1z']")
ac.click_and_hold(ele).move_by_offset(384,0).perform()
time.sleep(3)
derver.quit()