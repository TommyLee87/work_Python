# 1번 문제 : 세 자리 정수를 입력 받은 후 가장 큰 수 찾기

num = int(input("3자리 정수를 입력해주세요 : "))
a = num // 100
b = (num % 100) // 10
c = num % 10

if a > b:
    if a > c:
        print(f"가장 큰 수 : {a}")
    else:
        print(f"가장 큰 수 : {c}")
else :
    if b > c:
        print(f"가장 큰 수 : {b}")
    else:
        print(f"가장 큰 수 : {c}")


# 2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 : 9620
# 야간 : 주간 * 1.5
# 주간 근무[1], 야간 근무[2]를 입력하세요 :
# 근무 시간을 입력 하세요 :
# 입력한 시간 동안 주간 또는 야간 급여는 ___원 입니다.

day_or_night = int(input("주간 근무[1], 야간 근무[2]를 입력하세요 : "))
work_time = int(input("근무 시간을 입력하세요 : "))

if day_or_night == 1 :
    day_or_night = "주간"
    pay = work_time * 9620
else:
    day_or_night = "야간"
    pay = work_time * 9620 * 1.5

print(f"당신의 {day_or_night} 근무 {work_time}시간에 대한 급여는 {pay}원 입니다.")


# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 포인터 변수 s와 k에,
# 양의 정수를 정수형 변수 n에 각각 전달 받아 s문자열 뒤 부분의 n개 문자를 k문자열 앞에 끼워넣는 코드 작성
# s : seoul,  k : korea,  n : 2    ==> ulkorea

s = input("문자열 s 입력 : ")
k = input("문자열 k 입력 : ")
n = int(input("k문자열의 앞에 끼워넣을 글자 수 n 입력 : "))

print(s[-n:] + k)



