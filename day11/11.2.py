class PC:
    __size = ""
    __price = ""
    __cpu = ""
    __nc = 0
    __time = 0

    def setSize(self,size):
        self.__size = size
    def getSize(self):
        return self.__size

    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu = cpu
    def getCpu(self):
        return self.__cpu

    def setNc(self,nc):
        self.__nc = nc
    def getNc(self):
        return self.__nc

    def setTime(self,time):
        self.__time = time
    def getTime(self):
        return self.__time

    def dazi(self,work):
        print("我用我的",self.__size,"的大屏幕电脑",work)
    def playgame(self,gamename):
        print("下班之后，用",self.__cpu,"的电脑玩",gamename,"感觉太爽了！！！")
    def video(self,videoname):
        print("用",self.__size,"大屏幕看",videoname,"太过瘾了！！")
q = PC()
q.setNc("16")
q.setCpu("core i7")
q.setPrice("六千块")
q.setSize("32英寸")
q.setTime(24)
q.dazi("敲代码")
q.playgame("英雄联盟")
q.video("长歌行")