import  unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(r"D:\Py-workspace\pythonProject\银行对象版",pattern="Test*.py")
suite.addTest(tests)
f = open(file="银行测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "这是一个银行测试报告！",
    verbosity= 2,
    description = "执行了银行的用例"
)
runner.run(suite)