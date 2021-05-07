import random
import pymysql
from DBUtils import select
from DBUtils import update

users = {}
bank_name = "中国工商银行昌平支行"

def welcome():
    print("----------------------------")
    print("**    工商银行账户管理系统    **")
    print("----------------------------")
    print("* 1.开户                    *")
    print("* 2.存款                    *")
    print("* 3.取款                    *")
    print("* 4.转账                    *")
    print("* 5.查询                    *")
    print("* 6.退出                    *")
    print("----------------------------")

def bank_adduser(account,username,password,country,province,street,door):
    sql1 = "select count(*) from user"
    data = select(sql1,[])

    if data[0][0] >= 100:
        return 3
    sql2 ="select * from user where account = %s"
    param2 = [account]
    data2 = select(sql2,param2)
    if len(data2) != 0:
        return 2
    sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param3 = [account,username,password,country,province,street,door,0,bank_name]
    update(sql3,param3)
    return 1

def addUser():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "e", "f"]
    account = ""
    for i in range(8):
        index = random.randint(0,len(li)-1)
        account = account + li[index]
    username = input("请输入您的姓名：")
    password = input("请输入您的密码（6位数字）：")
    print("请完善您的地址信息")
    country = input("请输入您的国籍：")
    province = input("请输入您的省份：")
    street = input("请输入您的街道：")
    door = input("请输入门牌号：")
    start = bank_adduser(account,username,password,country,province,street,door)
    if start == 1:
        print("开户成功！！")
        info = '''
        ********个人信息********
        账号：%s,
        用户名：%s,
        密码：%s,
        地址信息：
         国籍：%s,
         省份：%s,
         街道：%s,
         门牌号：%s,
        余额：%s,
        开户行：%s
        ***********************
        '''
        print(info % (account,username,password,country,province,street,door,0,bank_name))
        if start == 2:
            print("该用户已存在！！！")
        if start == 3:
            print("该银行用户库已满！！！！")

def bank_addMoney(account,money):

    sql1 = "select account from user where user.account = %s"
    param1 = [account]
    data = select(sql1,param1)
    num = len(data)
    if num == 1:
        sql2 = "update user set money = money + %s where account = %s"
        param2 = [money,account]
        update(sql2,param2)
        return 1
    if num == 0:
        return False


def addMoney():
    account = input("请输入账号：")
    money = input("请输入存款金额：")
    start = bank_addMoney(account,money)
    if start == 1:
        print("存入成功！！！")
    if start == False:
        print("您输入的账号不存在！！")

def bank_moneyout(account,outmoney,password):

    sql = "select * from user where account =%s"
    date = select(sql,account)

    if len(date) != 0:
        sql1 = "select account from user where password = %s"
        date1 =select(sql1,password)

        if len(date1) != 0:
            sql2 = "select * from user where account =%s and money >= %s"
            date2 = select(sql2,[account,outmoney])

            if len(date2)!=0:
                sql3 = "update user set money = money - %s where account = %s"
                update(sql3,[outmoney,account])

            else:
                return 3
        else:
            return 2
    else:
        return 1
def moneyout():
    account = input("请输入用户账号:")
    outmoney = input("请输入您要取的金额：")
    password = input("请输入您的取款密码：")
# 将数据传到银行
    status2 = bank_moneyout(account,outmoney,password)
    if outmoney.isdigit():
        if status2 == 1:
            print("您输入的账号不存在，请重新输入")
        elif status2 == 2:
            print("您的密码错误，请重新输入")
        elif status2 == 3:
            print("您的余额不足")
        else:
            print("取款成功")

    else:
        print("输入非法")

def bank_moneytransfer (account1,account2,password,moneytransfer):
    sql = "select * from user where account = %s"
    date = select(sql,account1)

    if len(date) != 0:
        sql2 = "select * from user where account = %s"
        date1 = select(sql2,account2)

        if len(date1) !=0:
            sql3 = "select * from user where account = %s and password = %s"
            date2 = select(sql3,[account1,password])

            if len(date2) !=0:
                sql4 = "select * from user where account= %s and money >=%s"
                date3 = select(sql4,[account1,moneytransfer])

                if len(date3)!=0:
                    sql5 = "update user set money = money - %s where account = %s"
                    update(sql5,[moneytransfer,account1])
                    sql6 = "update user set money = money +%s where account = %s"
                    update(sql6,[moneytransfer,account2])
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
def moneytransfer():
    account1 = input("请输入要转出的账户：")
    account2 = input("请输入要转入的账户：")
    password = input("请输入转出账户的密码：")
    moneytransfer = input("请输入要转账的金额：")
    if moneytransfer.isdigit():
# 将数据录入银行
        status3 = bank_moneytransfer(account1,account2,password,moneytransfer)
        if status3 == 0:
            print("成功转出：",moneytransfer,"元")
        elif status3 == 1:
            print("账号错误，请重新输入")
        elif status3 ==2:
            print("转出的账号密码错误")
        elif status3 == 3:
            print("转出的金额不足，请重新输入")
    else:
        print("输入非法")

def bank_seek(account, password):
    sql = "select * from user where account = %s"
    param = [account]
    date = select(sql,param)
    if date != 0:
        sql1 = "select * from user where account = %s and password = %s"
        param1 = [account, password]
        date1 = select(sql1,param1)
        if date1 != 0:
            return 0
        else:
            return 2
    else:
        return 1

def seek():
    account = input("请输入您的要查询的账号：")
    password = input("请输入密码：")

    sql = "select * from user where account = %s and password = %s"
    param = [account, password]
    data = select(sql,param)
    for i in data:
        account = data[0][0]
        username = data[0][1]
        password = data[0][2]
        cuntry = data[0][3]
        province = data[0][4]
        street = data[0][5]
        door = data[0][6]
        money = data[0][7]
        bank_name = data[0][8]
    start = bank_seek(account, password)
    if start == 0:
        print("以下为您的账号信息")
        info = '''
                    ----------- 个人信息-------------
                    账号： %s,
                    用户名： %s,
                    取款密码： %s,
                    地址信息： 
                            国家： %s,
                            省份： %s,
                            街道： %s,
                            门牌号： %s,
                    余额： %s,
                    开户行： %s
                    ---------------------------------
                    '''
        print(info % (account,username,password,cuntry,province,street,door,money,bank_name))
    if start == 1:
        print("该用户不存在")
    if start == 2:
        print("您输入的密码不正确")


while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            # 开户
            addUser()
        elif num == 2:
            # 存款
            addMoney()
        elif num == 3:
            # 取款
            moneyout()
        elif num == 4:
            # 转账
            moneytransfer()
        elif num == 5:
            # 查询
            seek()
        elif num == 6:
            print("欢迎下次光临！")
            break
        else:
            print("输入非法！！！请重新输入！！！")
    else:
        print("输入非法！！！请重新输入！！！")
