# 반복문 : 조건이 참인동안 계속 수행되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n :    # 파이썬은 정수 값이 0이 아니면 참으로 간주
#     sum += n
#     n -= 1   # 파이썬은 증감 연산자가 없음
# print(sum)

# while True:
#     age = int(input("나이를 입력 하세요 : "))
#     if age > 0 and age < 200:
#         print(f"당신의 나이는 {age} 입니다.")
#         break
#     print("나이 입력 범위를 벗어났습니다.")

# for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용 (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]
# for e in fruits:
#     print(e[0])
#
# print(fruits[3][1][0])  #3번 인덱스["seoul", "korea"]의 1번 인덱스("korea")의 0번 인덱스(k)
#
# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1:
#     print(e, end="*")

#for 변수 i range (시작값, 종료값, 증감값):
# n = int(input("정수를 입력하세요 : "))
# sum = 0
# for i in range(1, n+1):  # 1부터 n+1 미만까지
#     sum += i
# print(sum)

# for문을 역순으로 반복하기
# for i in range(10, -1, -2) : # 10에서부터 0까지, -1(하나씩 줄이면서), -2(2개단위로 나씩 건너뛰고) 출력
#     print(i)

# 이중 for문
# n = int(input("정수를 입력 하세요 : "))   #사각형찍기
# for i in range(0,n):
#     for j in range(0,n):
#         print("*", end=" ")
#     print()

# 구구단 찍기
# for i in range(2,10):   # 2단 ~ 9단
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")
#     print()

# 홀수/짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if j % 2 == 0:
#             print("=", end=' ')
#         else:
#             print("*", end=' ')
#     print()


# 사각형 찍기 연습
# 정수값 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 값은 1부터 시작
# n = int(input("정수 입력 : "))
#
#
# for i in range(1,n * n + 1):
#     print(f"{i:>2}", end=' ')
#     if i % n == 0:
#         print()

# 사각 기본 별찍기
# * * *
# * * *
# * * *

# n = int(input("정수를 입력 하세요 : "))   #사각형찍기
# for i in range(0,n):
#     for j in range(0,n):
#         print("*", end=" ")
#     print()


#별찍기1

# *
# * *
# * * *
# * * * *
# * * * * *
#
# n = int(input("별 갯수 입력 : "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()


# 별찍기2

# * * * * *
# * * * *
# * * *
# * *
# *

# n = int(input("별 갯수 입력 : "))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=' ')
#     print()


# 별찍기3

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n = int(input("별 갯수 입력 : "))
# for i in range(n):
#     for s in range(i):
#         print(" ", end=' ')
#     for s in range(n-i):
#         print("*", end=' ')
#     print()

# 별찍기4

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input("별 갯수 입력 : "))
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# 문자와 ASCII코드
#chr : 유니코드 값을 입력 받아 그 코드에 해당하는 문자를 출력
#ord : 문자를 유니코드 값으로 변환

# for i in range(ord("A"), ord("Z")+1) :
#     print(chr(i), end = " ")
# print()
#
# for i in range(65, 91) :
#     print(chr(i), end=" ")
# print()


