from selenium import webdriver
import time
chormDriver = webdriver.Chrome()
chormDriver .get("http://www.baidu.com")
chormDriver .maximize_window()
chormDriver .find_element_by_id("kw").send_keys("闪电")
chormDriver .find_element_by_id("su").click()
time.sleep(5)
chormDriver .quit()