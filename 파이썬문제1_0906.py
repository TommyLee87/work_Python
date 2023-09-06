# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초

hour, min, sec = map(int, input("시간 입력 : ").split(":"))
if hour > 12:
    hour -= 12
    print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
else:
    print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")

# 2. 3개의 정수를 입력 받아 최대값과 최소값 구하기

num1 = input("첫번째 정수 입력 : ")
num2 = input("두번째 정수 입력 : ")
num3 = input("세번째 정수 입력 : ")

if num1 > num2:
    if num1 > num3:
        print("최대값 : " + num1)
    else:
        print("최대값 : " + num3)
else:
    if num2 > num3:
        print("최대값 : " + num2)
    else:
        print("최대값 : " + num3)

if num1 < num2:
    if num1 < num3:
        print("최소값 : " + num1)
    else:
        print("최소값 : " + num3)
else:
    if num2 < num3:
        print("최소값 : " + num2)
    else:
        print("최소값 : " + num3)

# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
from datetime import datetime

curr_year = datetime.today().year
jumin = input("주민등록번호 : ")
year = int(jumin[:2])
mon = int(jumin[2:4])
day = int(jumin[4:6])
gender = int(jumin[7])

#생년월일
print(f"생년월일 : {year:02}년 {mon:02}월 {day:02}일")
#성별
if gender == 1 or 3:
    print("성별 : 남성")
else:
    print("성별 : 여성")
#나이
if gender == 1 or 2:
    age = curr_year - 1900 - year + 1
else:
    age = curr_year - 2000 - year + 1
print(f"나이 : {age}")

# 4. 갯수가 정해지지않은 여러개의 정수를 입력 받아 합계와 평균 구하기
# list 사용
score = list(map(int, input("정수 입력 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")
