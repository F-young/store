from selenium import webdriver
import time

b = webdriver.Chrome()
b.get(r"D:/Python自动化/练习的html/练习的html/上传文件和下拉列表/autotest.html")
b.find_element_by_xpath("//*[@id='accountID']").send_keys("灰太狼")
b.find_element_by_xpath("//*[@id='passwordID']").send_keys("love")
b.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
b.find_element_by_xpath("//*[@id='sexID2']").click()
b.find_element_by_xpath("//*[@value='spring']").click()
b.find_element_by_xpath("//*[@value='summer']").click()
b.find_element_by_xpath("//*[@value='Auterm']").click()
b.find_element_by_xpath("//*[@value='winter']").click()
b.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\dell\Pictures\QQ浏览器截图\美女.jpg")
b.find_element_by_xpath("//*[@id='buttonID']").click()
b.switch_to.alert.accept()
time.sleep(5)
b.quit()