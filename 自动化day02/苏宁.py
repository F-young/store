from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com")
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("iPhone")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='0000000000-12276724825']/div/div/div[3]/a[3]").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[16]/div[3]/div[1]/div[2]/a/div/div/span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='myCart']/div[3]/div/a").click()
time.sleep(5)
driver.quit()
