import unittest
from Bank import Bank
class TestTransfer(unittest.TestCase):
    def test_Transfer1(self):
        account1 = "ejeow215"
        account2 = "skasda22"
        password = 123456
        money = 20
        s = 1

        kh = Bank()
        start = kh.bank_transfer(account1,account2,password,money)
        self.assertEqual(s,start)
    def test_Transfer2(self):
        account1 = "ejeow216"
        account2 = "ediodw22"
        password = 123456
        money = 50
        s = 1
        kh = Bank()
        start= kh.bank_transfer(account1,account2,password,money)
        self.assertEqual(s,start)