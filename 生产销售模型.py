'''
六名厨师造面包，五人购买。柜台能放三百个，柜台满了，厨师停3秒。问
五分钟，厨师一共生产了多少个，顾客每人买了多少面包，花了多少钱。每个面包十元
'''
import threading
import  time
gt = 0
time_start = time.time()
class Chanxiao(threading.Thread):
    chfeNum = ""
    count = 0
    def run(self) -> None:
       global gt
       global time_start
       while True:
           if gt >= 300:
               print("柜台已满，请稍等三秒钟")
               time.sleep(3)
               continue
           else:
               gt = gt + 1
               self.count = self.count + 1
               print(self.chfeNum,"已经生产了",self.count,"个面包")
               time_end1 = time.time()
               time_c1 = time_end1 - time_start
               time_c1 = int(time_c1)
               if time_c1 >= 300:
                   break
               else:
                   continue
class Sale(threading.Thread):
    gkNum = ""
    gmsl = 0
    money = 0
    def run(self) -> None:
        global gt
        global time_start
        while True:
            if gt <= 0:
                print("柜台上已经么有了，厨师正在加紧时间做。请稍等")
            else:
                gt = gt - 1
                self.gmsl = self.gmsl + 1
                self.money = self.money + 10
                print(self.gkNum,"购买了",self.gmsl,"个面包，花了",self.money,"元！")
                time_end = time.time()
                time_c = time_end - time_start
                time_c = int(time_c)
                if time_c >= 300:
                    break
                else:
                    continue








c1 = Chanxiao()
c2 = Chanxiao()
c3 = Chanxiao()
c4 = Chanxiao()
c5 = Chanxiao()
c6 = Chanxiao()

gk1 = Sale()
gk2 = Sale()
gk3 = Sale()
gk4 = Sale()
gk5 = Sale()


c1.chfeNum =("厨师1")
c2.chfeNum =("厨师2")
c3.chfeNum =("厨师3")
c4.chfeNum =("厨师4")
c5.chfeNum =("厨师5")
c6.chfeNum =("厨师6")

gk1.gkNum =("顾客1")
gk2.gkNum =("顾客2")
gk3.gkNum =("顾客3")
gk4.gkNum =("顾客4")
gk5.gkNum =("顾客5")


c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()


gk1.start()
gk2.start()
gk3.start()
gk4.start()
gk5.start()

