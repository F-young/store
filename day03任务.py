num1 = int(input("请输入第1个数："))
num2 = int(input("请输入第2个数："))
num3 = int(input("请输入第3个数："))
num4 = int(input("请输入第4个数："))
num5 = int(input("请输入第5个数："))
num6 = int(input("请输入第6个数："))
num7 = int(input("请输入第7个数："))
num8 = int(input("请输入第8个数："))
num9 = int(input("请输入第9个数："))
num10 = int(input("请输入第10个数："))
Sn = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
print("这十个数的和为：",Sn)

while num1 < num2:
    num1 = num2
else:
    num2 = num1
while num1 < num3:
        num1 = num3
else:
        num3 = num1
while num1 < num4:
        num1 = num4
else:
        num4 = num1
while num1 < num5:
        num1 = num5
else:
        num5 = num1
while num1 < num6:
    num1 = num6
else:
    num6 = num1
while num1 < num7:
        num1 = num7
else:
        num7 = num1
while num1 < num8:
        num1 = num8
else:
        num8 = num1
while num1 < num9:
        num1 = num9
else:
        num9 = num1
while num1 < num10:
    num1 = num10
else:
    num10 = num1

print("最大的数是：",num1)
print("这十个数的平均数是：",(Sn/10))

import random

num = random.randint(49,151)
print(num)


