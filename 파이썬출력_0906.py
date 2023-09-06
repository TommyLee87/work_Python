# 파이썬의 다양한 출력 방법
name = "도리탕"
age = 20
gender = "남성"
jobs = "소프트웨에 개발자"
addr = "서울시 광진구 자양동"

# C언어 스타일 : 서식지정자를 사용하는 방식
print("=" * 5, "C 스타일", "=" * 5)
print("이름 : %s" % name)
print("나이 : %d" % age)
print("성별 : %s" % gender)
print("직업 : %s" % jobs)
print("주소 : %s" % addr)

# 파이썬 스타일 : 3.6 이전 방법
print("=" * 5, "Python 3.6 이전 스타일", "=" * 5)
print("이름 : {} / {}".format(name, addr))
print("나이 : {}".format(age))

# 파이썬 현재 스타일 : 3.6 이후 방식, f와 {} 사용해서 출력하는 방식
print("=" * 5, "Python 현재 스타일", "=" * 5)
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}, 직업 : {jobs}")

# 자바 스타일 : 문자열 연결 방법 (+)
print("=" * 5, "Java 스타일", "=" * 5)
print("이름 : " + name)
print("나이 : " + str(age))
print("주소 : " + addr)

# 출력 시 정렬하기
# < 좌측 정렬
# > 우측 정렬, 생략 가능
# ^ 중앙 정렬
print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:^6}|".format(10))

num = 10
print(f"|{num:>5}|")
print(f"|{num:<5}|")
print(f"|{num:^6}|")
PI = 3.14159265359
print(f"{PI:.4f}")  # 소수점 4자리까지
