import random

sp = [
    ["孜然味青草",10],
    ["烧烤狼排味青草",20],
    ["香草味青草",20],
    ["兰花味青草",30],
    ["番茄味青草",10],
    ["冰淇淋味青草",30],
    ["红太狼同款指甲油",50],
    ["狼皮大衣",250],
    ["喜羊羊同款铃铛",80],
    ["红太狼同款平底锅",100]

]
yhq = [
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["烧烤狼排味优惠券","满100减30"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],
    ["平底锅优惠券","半折甩卖"],

]
print("********欢迎来到青青草原交互商城********")
zl = random.randint(0,len(yhq)-1)
youryhq = yhq[zl]
print("您获得的优惠券为：",youryhq)
if zl < 10:
    yh = 1
    yh = int(yh)
else:
    yh = 0
    yh = int(yh)

salary = input("请输入您的薪资：")
salary = int(salary)
salary1 = salary
yourcart = []
sl = 0
mycart = []
while True:
    for index,value in enumerate(sp):
        print(index," ",value)
    num = input("请输入您要购买的物品编号：")
    if num.isdigit():
        num = int(num)
        if num >= len(sp):
               print("商品不存在，请重新选择：")
        else:
            if salary >= sp[num][1]:

                   sl = input("请输入您要购买的数量：")
                   sl = int(sl)
                   #yourcart.append(sp[num])
                   #yourcart.append(sl)
                   #mycart.append(yourcart)

                   if num == 1 and sp[num][1] * sl > 100 and yh == 1:
                       salary = salary - sp[num][1] * sl + 30
                   elif num == 9 and yh == 0:
                       salary = salary - sp[num][1] / 2 * sl
                   elif salary - sp[num][1] * sl <= 0:
                       print("对不起，您的余额不足！！")
                   else:
                       salary = salary - sp[num][1] * sl
                   if salary < 0:
                       print("对不起，您的余额不足！")
                   else:
                       print("成功添加到购物车！！！余额为：", salary)
                       yourcart.append(sp[num])
            else:
                   print("对不起，穷鬼，您的余额不足！！！")
    elif num == "Q" or num == "q":
           print("***********欢迎下次光临***********")
           break
    else:
           print("输入非法，请重新输入！！！！")


jf = (salary1 - salary) / 10
print("本次您购买的商品如下：")
for index,value in enumerate(yourcart):
       print(index," ",value)
print("您的余额为：",salary,"您本次消费获取的积分为：",jf)
print(yourcart)

