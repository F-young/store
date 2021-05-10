f1 = open(file="scores.txt",mode="r+",encoding="utf-8")
f2 = open(file="sum.txt",mode="w+",encoding="utf-8")
data = f1.readlines()
sum = 0
for i in data:
    da1 = i.replace("\n","").split(" ")
    name = da1[0]
    da2 = da1
    del da2[0]
    for i in da2:
        i = int(i)
        sum = sum + i
    f2.write(name )
    f2.write(str(sum))
    f2.write("\n")
f1.close()
f2.close()

