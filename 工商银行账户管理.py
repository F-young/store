import random
import pymysql

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
    con = pymysql.connect(host='localhost',user='root',password='root',database='bank')
    cursor = con.cursor()
    sql = "select account from user"
    num = cursor.execute(sql)
    if num >= 100:
        return 3
    else:
        sql01="select account from user where user.account = %s"
        param01=[account]
        cursor.execute(sql01,param01)
        data =cursor.fetchall()
        num =len(data)
        if num == 1:
            return 2
        if num == 0:
            sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = [account,username,password,country,province,street,door,0,bank_name]
            cursor.execute(sql,param)
            con.commit()
            return 1
    con.close()
    cursor.close()

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
    con = pymysql.connect(host='localhost',user='root',password='root',database='bank')
    cursor = con.cursor()
    sql = "select account from user where user.account = %s"
    param = [account]
    cursor.execute(sql,param)
    data = cursor.fetchall()
    num = len(data)
    if num == 1:
        sql = "update user set money = money + %s where account = %s"
        param = [money,account]
        cursor.execute(sql,param)
        con.commit()
        return 1
    if num == 0:
        return False
    con.close()
    cursor.close()
def addMoney():
    account = input("请输入账号：")
    money = input("请输入存款金额：")
    start = bank_addMoney(account,money)
    if start == 1:
        print("存入成功！！！")
    if start == False:
        print("您输入的账号不存在！！")

def bank_withdrawal(account,password,getmoney):
    con = pymysql.connect(host='localhost', user='root', password='root', database='bank')
    # 创建控制台
    cursor = con.cursor()
    # 查询表中数据
    sql = "select account from user where user.account = %s"
    param = [account]
    # 执行sql
    cursor.execute(sql, param)
    # 获取到数据
    data = cursor.fetchall()
    # 获取是否存在输入的account
    num = len(data)

    if num == 1:
        sql = "select password from user where user.account = %s and user.password = %s"
        param = [account, password]
        num = cursor.execute(sql, param)
        if num == 1:
            sql = "update user set user.money =user.money - %s where user.money >= %s"
            param = [getmoney, getmoney]
            num = cursor.execute(sql, param)
            con.commit()
            if num == 1:
                return 0
            if num == 0:
                return 3
        if num == 0:
            return 2
    else:
        return 1
    # 关闭资源
    con.close()
    cursor.close()

def withdrawal():
    account = input("请输入账号：")
    password = input("请输入密码：")
    getmoney = input("请输入要取出的金额：")

    start = bank_withdrawal(account, password, getmoney)
    if start == 0:
        print("取款成功！")
    if start == 1:
        print("账号不存在！")
    if start == 2:
        print("密码不对")
    if start == 3:
        print("账户余额不足")

def bank_transfer(account1, account2, password, money):
    con = pymysql.connect(host='localhost', user='root', password='root', database='bank')
    cursor = con.cursor()
    sql = "select account from user where user.account = %s or user.account = %s"
    param = [account1, account2]
    num = cursor.execute(sql, param)

    if num == 2:
        sql = "select account from user where user.account = %s and user.password = %s"
        param = [account1, password]
        num = cursor.execute(sql, param)
        if num == 1:
            sql = "update user set user.money = user.money - %s where user.account = %s"
            param = [money, account1]
            num = cursor.execute(sql, param)
            con.commit()
            sql1 = "update user set user.money = user.money + %s where user.account = %s"
            param1 = [money, account2]
            num1 = cursor.execute(sql1, param1)
            con.commit()
            if num == 1 and num1 == 1:
                return 0
            else:
                return 3
        if num == 0:
            return 2
    else:
        return 1
    con.close()
    cursor.close()

def transfer():
    account1 = input("请输入您要转出的账号：")
    account2 = input("请输入您要转入的账号：")
    password = input("请输入您转出账号的密码：")
    money = input("请输入您要转出的金额：")

    start = bank_transfer(account1, account2, password, money)
    if start == 0:
        print("转账成功！")
    if start == 1:
        print("您输入的账号不正确！")
    if start == 2:
        print("您输入的密码不正确！")
    if start == 3:
        print("您的账户余额不足！")


def bank_seek(account, password):
    # 获取数据库连接
    con = pymysql.connect(host='localhost', user='root', password='root', database='bank')
    # 创建控制台
    cursor = con.cursor()
    # 查询表中数据
    sql = "select * from user where account = %s"
    param = [account]
    # 执行sql
    num = cursor.execute(sql, param)
    if num == 1:
        sql = "select * from user where account = %s and password = %s"
        param = [account, password]
        num = cursor.execute(sql, param)
        date = cursor.fetchall()
        print(date)
        if num == 1:
            return 0
        if num == 0:
            return 2
    if num == 0:
        return 1
    con.close()
    cursor.close()

def seek():
    account = input("请输入您的要查询的账号：")
    password = input("请输入密码：")
    # 获取数据库连接
    con = pymysql.connect(host='localhost', user='root', password='root', database='bank')
    # 创建控制台
    cursor = con.cursor()
    # 查询表中数据
    sql = "select * from user where account = %s and password = %s"
    param = [account, password]
    # 执行sql
    cursor.execute(sql, param)
    data = cursor.fetchall()
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
            withdrawal()
        elif num == 4:
            # 转账
            transfer()
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
