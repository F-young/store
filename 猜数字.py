import random
num =random.randint(0,101)
gold = 10000
count =0
print("你每猜错一次将扣除500金币，猜中奖励3000金币")
while True:
    count = count + 1
    gold = gold - 500
    num1 = input("请输入你猜的数字：")
    num1 = int(num1)
    if num1 > num and count <7:
        print("大了！你已经猜了",count,"次！剩余金币为：",gold)
    elif num1 < num and count < 7:
        print("小了！！你已经猜了",count,"次！剩余金币为：",gold)
    elif count >= 7:
        print("对不起，七次未猜中，游戏结束！！剩余金币为：",gold)
        break
    else:
        print("恭喜你猜对了，本次幸运数字为：", num, "你一共猜了", count, "次！你剩余的金币为：", gold + 3000, )
        break