from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.huya.com")
driver.find_element_by_xpath("//*[@id='search-bar-input']").send_keys("萝莉酱")
driver.find_element_by_xpath("//*[@id='searchForm_id']/button").click()
time.sleep(3)
wins = driver.window_handles
print(wins)
driver.switch_to.window(wins[1])
driver.find_element_by_xpath("//*[@id='js-host-list']/li[1]/a").click()
time.sleep(6)
driver.switch_to.window(wins[0])
driver.quit()