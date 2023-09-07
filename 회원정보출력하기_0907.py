# 이름 입력
# 나이 입력 : 1 ~ 199, 잘못 된 값은 재 입력 요청
# 성별 입력 : 영문 'm'과'M'은 남성, 'f'와'F'는 여성
# 직업 입력 : 1.학생   2.회사원   3.주부   4.무직, 잘못된 값은 재입력
# 결과를 한번에 출력

name = input("이름을 입력하세요 : ")

while True:
    age = int(input("나이를 입력하세요 : "))
    if age < 0 or age > 200:
     print("다시 입력해주세요.")
    else:
        break

while True:
    gender = input("성별을 입력하세요 : ")
    if gender == "M" or gender == "m":
        gender = "남성"
        break
    elif gender == "F" or gender == "f":
        gender = "여성"
        break
    else:
        print("다시 입력해주세요.")

while True:
    print("직업에 맞는 번호를 입력하세요.")
    jobs = int(input("[1]학생 [2]회사원 [3]주부 [4]무직 : "))
    if jobs == 1:
        jobs = "학생"
        break
    elif jobs == 2:
        jobs = "회사원"
        break
    elif jobs == 3:
        jobs = "주부"
        break
    elif jobs == 4:
        jobs = "무직"
        break
    else:
        print("다시 입력해주세요.")

print("=" * 10 + " 회원 정보 " + "=" * 10)
print(f"\n이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs}")