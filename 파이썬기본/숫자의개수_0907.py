# A = 150, B = 266, C = 427 이라면 A * B * C = 150 * 266 * 427 = 17037300
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력

# a, b, c = map(int, input("정수 3개 입력 : ").split())
a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))
c = int(input("세 번째 정수 입력 : "))

total_val = str(a * b * c)    # a * b * c 의 결과를 문자열로 반환

for i in range(10):
    print(total_val.count(str(i)))
