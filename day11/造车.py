class Car:
    num = 0
    color = ""
    sites = ""
    brand = ""
    weight = 0

    def run(self):
        print(self.num ,"个轮子的",self.color ,self.brand, "正在大马路上跑来跑去！！！太羡慕了！！！")


c = Car()
c.num = 6
c.color = "红色"
c.weight = "8000kg"
c.brand = "大卡"
c.run()

class Ren:
    name = ""
    sex = ""
    age = 0
    height = 0
    weight = 0
    hair = ""
    clothes = ""
    def dance(self):
        print("身高",self.height,"体重",self.weight,"穿着",self.clothes,"的",self.name,"正在跳广场舞！！！美极了")
a = Ren()
a.name = "老王"
a.sex = "男"
a.age = 58
a.height = 165
a.weight = 180
a.clothes = "比基尼"
a.dance()


