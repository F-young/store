import  unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(r"D:\Py-workspace\pythonProject\自动化day03",pattern="*Test.py")
suite.addTest(tests)
f = open(file="网页登录.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "这是一个网页登录测试报告！",
    verbosity= 2,
    description = "执行了登录的用例"
)
runner.run(suite)