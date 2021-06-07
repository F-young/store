from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'driverName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.jingdong.app.mall',
    'appActivity': 'com.jingdong.app.mall.main.MainActivity'
}


driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(3)
driver.find_element_by_id("bqd").click()
time.sleep(3)
driver.find_element_by_id("bq").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@content-desc='我的']").click()
time.sleep(3)
driver.quit()
