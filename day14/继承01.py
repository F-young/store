class OldPhone(object):
    __pinpai = ""
    def setPinpai(self,pinpai):
        self.__pinpai = pinpai
    def getPinpai(self):
        return self.__pinpai

    def call(self,phone):
        print("正在给",phone,"打电话.....")

class NewPhone(OldPhone):
    def call(self,phone):
        super().call(phone)
        print("正在拨号中.....")
    def jieshao(self):
        print("品牌为：",self.getPinpai(),"的手机真好用。。。")
new = NewPhone()
new.setPinpai("华为")
new.call("苹果")
new.jieshao()

