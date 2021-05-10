f1 = open(file="D:\Python学习文件\day10\gra.jpg",mode="rb")
f2 = open(file="D:\Python\gra1.jpg",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()
