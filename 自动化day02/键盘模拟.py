from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.suning.com")
ac = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='searchKeywords']")
ac.key_down("i",ele).perform()
time.sleep(2)
ac.key_up("i",ele).perform()
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)
driver.quit()