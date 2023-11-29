# 산술 연산자 : 사칙 연산자(+,-,*,/), 몫(//), 제곱 연산자(**), 나머지 연산자(%)
i = 10  # 파이썬은 데이터 형이 없기 때문에 값을 대입할 때 데이터 형이 결정 됨
j = 3
print(f"덧셈 : {i+j}")
print(f"뺄셈 : {i-j}")
print(f"곱셈 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱연산 : {i**j}")
test = "Python !!! "
print(test + "Hello")
print(test + str(100))
print(test * 3)  # test 문자열을 3번 반복
i += 1 ## 파이썬은 증감 연산자가 없음
print(f"증감연산자 시험 : {i}")

# 간단 예제 : 파이썬은 변수를 상수로 만드는 방법이 없으며, 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주
# TAX_RATE = 0.10
# income = int(input("당신의 수입은 얼마입니까? "))
#
# print(f"당신이 내야 할 세금은 {income * TAX_RATE:.2f} 입니다.")   # :.2f   소수점 2자리까지.

# 관계 연산자 : AND(&&) => and, OR(||) => or, NOT(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y  # False
rst2 = x > 0 or x > y  # True
rst3 = not(x > 0 or x > y)  # False
print(rst1,rst2,rst3, sep = "\n")

# 다항(3항) 연산자
num = int(input("정수 입력 : "))
# jAva : (num % 2 == 0)? "짝수" : "홀수"
# 람다 : e => (e % 2 == 0) and "짝수" or "홀수"
rst = (num % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

# 2진수 입력받기(0b)
number = 0b101010101
# 8진수 입력받기(0o)
number = 0o1234567
# 16진수 입력받기(0x0123456789abcdef)
number = 0xffffff