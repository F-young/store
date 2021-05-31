from selenium import webdriver
import time
a = webdriver.Chrome()
a.get(r"D:/Python自动化/练习的html/练习的html/弹框的验证/dialogs.html")
a.find_element_by_xpath("//*[@id='alert']").click()
time.sleep(5)
a.switch_to.alert.accept()
time.sleep(5)
a.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(5)
a.switch_to.alert.dismiss()
time.sleep(5)
a.quit()

