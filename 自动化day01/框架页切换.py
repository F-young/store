from selenium import webdriver
import time

w = webdriver.Chrome()
w.get(r"D:/Python自动化/练习的html/练习的html/main.html")
w.switch_to.frame("frame")
w.find_element_by_xpath("//*[@id='input1']").send_keys("被发现了")
time.sleep(5)
w.quit()