class TV:
    cnt = 0 # 클래스 맴버
    def __init__(self, name, isOn, channel, volume):
        self.__name = name # __변수 이름은 private 특성으로 간주됨.
        self.__isOn = isOn
        self.__channel = channel
        self.__volume = volume
        TV.cnt += 1
    def set_on(self, isOn):
        self.__isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.__channel = cnl
        else :
            print("채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.__volume = vol
    def get_on(self):
        return self.__isOn
    def get_channel(self):
        return self.__channel
    def get_volume(self):
        return self.__volume
    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.__name}")
        print(f"전원 : {power[self.__isOn]}")
        print(f"채널 : {self.__channel}")
        print(f"볼륨 : {self.__volume}")

lg_tv = TV("LG", True, 10, 20)
sam_tv = TV("LG", True, 10, 20)
lg_tv.__name = "SAMSUNG" # 에러는 안나지만 변경은 안됨
lg_tv.__isOn = False # 에러는 안나지만 변경은 안됨
lg_tv.set_channel(999)
lg_tv.view_tv()
print(TV.cnt)