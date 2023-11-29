# 오버라이딩 : 부모클래스를 상속받아 동일한 메소드에 대해 재정의해서 사용하는 것
# 오버로딩 : 1. 파이썬은 오버로딩이 없음(데이터형이 없어 매개변수를 아무거나 넣어도 동작하므로 오버로딩과 유사한 효과)
          # 2. 디폴트 매개변수 문법이 있음

class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume
    def set_on(self, isOn):
        self.isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.isOn
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume

class TV(ProtoTV):  # ProtoTV 로부터 상속받음
    def set_channel(self, cnl):  # 부모가 가진 메소드를 상속받아 재정의(오버라이딩)
        if 0 < cnl < 2000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")

lg_tv = TV(False,10,10)
