import unittest
from Bank import Bank
class TestWithRawal(unittest.TestCase):
    def test_AddUser1(self):
        account = "ejeow215"

        password = 123456
        getmoney = 500
        s = 2

        kh = Bank()
        start= kh.bank_withdrawal(account,password,getmoney)
        self.assertEqual(s,start)
    def test_AddUser2(self):
        account = "ejeow216"
        password = 123456
        getmoney = 10
        s = 2

        kh = Bank()
        start= kh.bank_withdrawal(account,password,getmoney)
        self.assertEqual(s,start)