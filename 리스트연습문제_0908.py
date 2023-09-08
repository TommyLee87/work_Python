# 1번 : 상근날드 (초급)
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거, 음료는 콜라와 사이다 두 종류
# 입력 : 연속 3버거, 2음료 가격
# 출력 : 햄버거 3종 중 가장 싼메뉴 + 음료 2종 중 싼메뉴 - 50

# food = list(map(int, input().split()))
# min_b = min(food[:3])
# min_d = min(food[3:5])

# print(f"{min_b + min_d - 50}")


# 2번 : 저항(중급)

color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

color_a = color.index(input("첫 번째 색상 입력 : "))
color_b = color.index(input("두 번째 색상 입력 : "))
color_c = 10 ** color.index(input("세 번째 색상 입력 : "))

print(int(str(color_a) + str(color_b)) * color_c)


# 3번 : PC방 알바(중급)

# 1번부터 100번까지 컴퓨터
# 첫째 줄에 손님의 수 N
# 들어오는 손님은 모두 자기가 앉고 싶은 자리, but 예약석은 거절
# 거절 당하는 사람의 수를 출력하는 프로그램을 작성

# seat_num = list(map(int, input().split()))
# pc = [0] * 100   # 100 개의 리스트(자리) 생성
# cnt = 0
# for e in seat_num:  # 향상된 for 문으로 e값은 고객이 앉고 싶은 자리 번호
#     if pc[e - 1] != 0:
#         cnt += 1
#     else:
#         pc[e - 1] = 1
# print(cnt)


# 4번 : Kaaaa-Maaa-Paaa => KMP,   Micro-Soft => MS

# upper_str = ""
# for e in input(): # 입력 받는 개수 만큼 자동 순회
#     if e.isupper():
#         upper_str += e
# print(upper_str)


