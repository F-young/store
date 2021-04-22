name = "root"
password = "admin"
password1 = input("请输入密码：")
count = 0
while True:
    count = count + 1
    if   password1 != password and count < 3:
           password1 =input("请输入密码：")
    elif count >= 3:
        print("输入三次密码错误，账号已锁定！")
        break
    else:
         print("登录成功")
         break