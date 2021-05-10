a = input("请输入证件的路径：")
b = input("请输入您的姓名：")
c = "D:\Python\ "
d = c + b +".jpg"
print(d)
f1 = open(file= a,mode="rb")
f2 = open(file= d,mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()

