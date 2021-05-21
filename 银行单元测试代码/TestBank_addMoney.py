import unittest
from Bank import Bank
class TestAddMoney(unittest.TestCase):
    def test_AddMoney1(self):
        account = "ejeow215"
        money = 10000
        kh = Bank()
        s = 1
        start= kh.bank_addMoney(account,money)
        self.assertEqual(s,start)
    def test_AddMoney2(self):
        account = "ejeow216"
        money = 100
        kh = Bank()
        s = 1
        start = kh.bank_addMoney(account,money)
        self.assertEqual(s,start)