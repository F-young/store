class Chushi(object):
    __name = ""
    __age = ""
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def rice(self):
        print("蒸饭")

class chushiSon(Chushi):
    def dish(self):
        print("炒菜")
class chushiSun(chushiSon,Chushi):
    def rice(self):
        print("正在蒸饭")
    def dish(self):
        print("正在炒菜")

test = chushiSun()
test.setName("狗蛋")
test.setAge("18")
print(test.getName(),test.getAge())


c = chushiSun()
c.rice()
c.dish()


