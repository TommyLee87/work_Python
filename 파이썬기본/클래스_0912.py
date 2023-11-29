# 생성자는 클래스가 객테로 만들어 질 때 자동으로 호출되며, 객체의 초기값을 지정할 수 있음.
# 생성자 키워드 : __init__
# self는 자신의 객체를 가리키는 변수
class TV:
    def __init__(self, name, is_on, channel, volume):
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def channel(self, cnl):
        self.channel = cnl
    def volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.is_on
    def view_tv(self):
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {self.is_on}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = TV("LG", False, 10, 10)
lg_tv.view_tv()
samsung_tv = TV("SAMSUNG", False, 20, 20)
samsung_tv.view_tv()

