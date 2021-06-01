from selenium import webdriver
from selenium.webdriver import ActionChains
import time
dri = webdriver.Chrome()
dri.get("https://www.qcc.com")
time.sleep(5)
dri.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()

time.sleep(3)
dri.find_element_by_link_text("登录 | 注册").click()
time.sleep(6)
ele = dri.find_element_by_xpath("//*[@id='nc_1_n1z']")
ac = ActionChains(dri)
ac.click_and_hold(ele).move_by_offset(348,0).perform()
time.sleep(7)
dri.quit()