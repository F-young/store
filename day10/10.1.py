import pymysql
con = pymysql.connect(host="localhost",user= "root",password="root",database = "净资产统计")
cursor = con.cursor()
print(con)
f = open(file="用户数据.txt",mode="r+")
data = f.readlines()
users = []
for i in data:
    da = i.replace("\n","").split(",")
    users.append(da)
sql = "insert into 详细信息 values(%s,%s,%s)"
zczh = 0
for j in users:
    cursor.execute(sql,j)
    con.commit()
    m = int(j[2])
    zczh = zczh + m
print("资产总和为：", zczh)
cursor.close()
con.close()
