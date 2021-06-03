from ddt import ddt
from ddt import data
from ddt import unpack
from selenium import webdriver
import unittest
from InitPage import InitPageData
from LoginOpera import LoginPage
import time
@ddt
class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jasonisoft.cn:8080/HKR")
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    @data(*InitPageData.success_data)
    def test_success_login(self,testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"],testdata["password"])
        result = login.get_success_login()
        expect = testdata["expect"]
        self.assertEqual(expect,result)

    @data(*InitPageData.password_error_data)
    def test_error_password_login(self,testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"],testdata["password"])
        result = login.get_error_password_login()
        expect = testdata["expect"]
        self.assertEqual(expect,result)