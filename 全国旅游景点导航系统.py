import random
city = {
    "北京":{
        "昌平":{
            "回龙观":["永辉","永旺"],
            "龙泽":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","五道口切糕"],
            "香山":["香山","植物园"],
            "高校":["清华","北大"]
        },
        "朝阳":{
            "朝阳南北塔":["世纪公园","玉渊潭公园"],
            "双塔":["双塔白醋"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡"]
        }
    },
    "天津":{
        "静海" : {
            "独流": ["独流老醋","小吃一条街"],
            "静海镇": ["我也不知道有啥","随便逛逛吧"]
        },
        "滨海新区" : {
            "渤海湾":["沙滩","海鲜","这些地方我也不知道有没有，我没去过"],
            "曲艺文化中心" : ["德云社","中心体育馆","这些地方我也不知道有没有，我没去过"]
        }
    },# 狗不理不好，麻花，煎饼果子
}

# 展示城市下列的方法
def print_place(data):
    for i in data:
        print(i)

while True:
    print("----------------------欢迎来到Jason全国旅游文化有限公司----------------------")
    print_place(city)
    num1 = input("请输入您要去的城市>>>:")
    if num1 in city: # 北京，天津
        print_place(city[num1])  #num1
        num2 = input("请输入二级城市>>>:")
        if num2 in city[num1]:
            print_place(city[num1][num2])
            num3 = input("请输入三级城市>>>:")
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])

                print("祝您旅途愉快！！")
                gw = input("请问您需要购物吗？请输入0 或1,0代表否，1代表是：")
                gw = int(gw)
                if gw == 1:


                    sp = [
                        ["孜然味青草", 10],
                        ["烧烤狼排味青草", 20],
                        ["香草味青草", 20],
                        ["兰花味青草", 30],
                        ["番茄味青草", 10],
                        ["冰淇淋味青草", 30],
                        ["红太狼同款指甲油", 50],
                        ["狼皮大衣", 250],
                        ["喜羊羊同款铃铛", 80],
                        ["红太狼同款平底锅", 100]

                    ]
                    yhq = [
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["烧烤狼排味优惠券", "满100减30"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],
                        ["平底锅优惠券", "半折甩卖"],

                    ]
                    print("********欢迎来到青青草原交互商城********")
                    zl = random.randint(0, len(yhq) - 1)
                    youryhq = yhq[zl]
                    print("您获得的优惠券为：", youryhq)
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
                        for index, value in enumerate(sp):
                            print(index, " ", value)
                        num = input("请输入您要购买的物品编号：")
                        if num.isdigit():
                            num = int(num)
                            if num >= len(sp):
                                print("商品不存在，请重新选择：")
                            else:
                                if salary >= sp[num][1]:

                                    sl = input("请输入您要购买的数量：")
                                    sl = int(sl)
                                    # yourcart.append(sp[num])
                                    # yourcart.append(sl)
                                    # mycart.append(yourcart)

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
                    for index, value in enumerate(yourcart):
                        print(index, " ", value)
                    print("您的余额为：", salary, "您本次消费获取的积分为：", jf)
                else:
                    print("对不起，打扰了，祝您旅途愉快！！！")

            elif num3 == "Q" or num3 == "q":
                print("欢迎下次光临！！！")
            else:
                print("对不起，输入有误，重新输入！！")
        elif num2 == "Q" or num2 == "q":
            print("欢迎下次光临！！！")
        else:
            print("对不起，输入有误，重新输入！！")

    elif num1 == "Q" or num1 == "q":
        print("欢饮下次光临！！！")
        break
    else:
        print("您输入的城市不存在！别瞎弄！！！！")























