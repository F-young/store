# encoding=utf-8

from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'driverName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
}


driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(10)
driver.find_element_by_id("bdb").click()
while True:
    time.sleep(5)
    driver.swipe(421,856,421,266,200)

