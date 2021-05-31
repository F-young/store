from selenium import webdriver
import time
q = webdriver.Chrome()
q.get(r"D:/Python自动化/练习的html/练习的html/frame.html")
#输入
q.find_element_by_xpath("//*[@id='input1']").send_keys("叫爸爸")
time.sleep(5)
#清空
q.find_element_by_xpath("//*[@id='input1']").clear()
time.sleep(5)
q.quit()