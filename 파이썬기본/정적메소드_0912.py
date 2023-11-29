class Car :
    isinstance_count = 0

    # 초기화 함수
    def __init__(self, size, model):
        self.size = size   # 인스턴스 변수 생성 및 초기화
        self.model = model
        Car.isinstance_count = Car.isinstance_count + 1 # 클래스 변수 이용
        print(f"자동차 객체 생성 수 : {Car.isinstance_count}")

    def move(self, speed):
        self.speed = speed
        print(f"{self.size} & {self.model} 자동차가 시속 {self.speed}km로 달립니다.")


    # 클래스 소속, 객체로 만들어지지 않음
    def check_type(code):
        if(code >= 10 and code < 20): print("전기차 입니다.")
        elif(code >= 20 and code < 30): print("가솔린차 입니다.")
        elif(code >= 30): print("디젤차 입니다.")
        else: print("분류 코드가 없습니다.")

car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")
car1.move(90)
Car.check_type(20)
car2.move(70)
