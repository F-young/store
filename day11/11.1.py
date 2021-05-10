class Cup:
    __height = 0
    __rj = ""
    __color = ""
    __cz = ""
    def setHeight(self,height):
        self.__height  = height
    def getHeight(self):
        return self.__height

    def setRj(self,rj):
        self.__rj = rj
    def getRj(self):
        return self.__rj

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setCz(self,cz):
        self.__cz = cz
    def getCz(self):
        return self.__cz

    def cfye(self):
        print("我有一个高",self.__height ,self.__color ,"的",self.__cz ,"杯子。")
b = Cup()
b.setHeight(25)
b.setRj("1500ml")
b.setColor("棕色")
b.setCz("玻璃")
yt = "饮料"
b.cfye()


