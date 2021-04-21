IDnum = input("请输入身份证编号：")
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
height = input("请输入身高：")
add = input("请输入居住地址：")
info = ''''
**************个人信息录入**************
身份证编号：%s,
姓名：%s,
年龄：%s,
性别：%s,
身高：%s,
居住地址：%s
**************************************
'''
print(info  %  (IDnum,name,age,sex,height,add))