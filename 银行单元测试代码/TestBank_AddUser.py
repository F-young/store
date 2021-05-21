import unittest
from Bank import Bank
class TestAddUser(unittest.TestCase):
    def test_AddUser1(self):
        account = "ejeow215"
        username = "fyy"
        password = 123456
        counrry = "cn"
        province = "hb"
        street = "cp"
        door = "0002"
        start = 1

        kh = Bank()
        jg= kh.bank_addUser(account,username,password,counrry,province,street,door)
        self.assertEqual(start,jg)
    def test_AddUser2(self):
        account = "ejeow216"
        username = "懒羊羊"
        password = 123456
        counrry = "cn"
        province = "hb"
        street = "cp"
        door = "0006"
        start= 1
        kh = Bank()
        jg= kh.bank_addUser(account,username,password,counrry,province,street,door)
        self.assertEqual(start,jg)


