# 크기가 정해지지 않은 요소들의에 값을 저장하기 위한 자료형
# 자료형의 제한이 없다.
# 중첩 사용이 가능하다. [ [], [] ,[[],[]],[[]], ]
# 뮤터블 객체 (읽고 쓰기가 가능)

# number = [1, 2, 3, 4, 5, 6]
# fruits = ["apple", "banana", "orange"]
# mixed = [1, True, "seoul", 3.1415]
# dup = [1, [1, 2, 3, 4, 5], ["apple", "banana"], "orange"]


# 변수와 리스트를 비교 해보기
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# print(sum([kor, eng, mat]))


# 리스트는 성적의 개수에 상관없이 입력 받을 수 있음
# score = list(map(int, input("성적 입력 : ").split()))
# print(sum(score)/len(score))


# 인덱싱과 슬라이싱
# str_name = ["seoul", "gangnam", "gwangjingu", "daegu", "inchon"]
# 인덱싱
# print(str_name)  # 리스트 전체 출력
# print(str_name[1])  # 1번째 요소 출력
# print(str_name[1][2])  # 1번째 요소의 2번째 문자열

# 슬라이싱
# slice = str_name[1:3]  # 1번에서 3번 미만까지
# print(slice)
# print(len(slice[0]))

# primes = [2, 3, 5, 7]
# print(primes[0])
# print(primes[-1])
# print(primes[-2:])


# 리스트 연산자 : 연결(+), 반복(*), len()
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a + list_b)
# print(list_a * 3)
# print(len(list_a + list_b))


# 리스트 요소 추가하기 : append() : 리스트의 맨 마지막에 추가,insert(index, 값) : 해당 인덱스에 값을 삽입
# list_a = [1, 2, 3]
# list_a.append(4)
# list_a.append(5)
# list_a.insert(1, 10)
# print(list_a)


# 리스트 제거하기 : pop(), remove(), clear(), del 리스트명[인덱스]
# pop() : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제, 인덱스가 있으면 해당 위치의 값을 삭제
# remove(값) :  해당하는 값을 제거, 만약 동일한 값이 여러개면 낮은(앞쪽) 인덱스값 제거
# clear() : 모든 값을 삭제, 리스트는 지우지 않음 (빈 리스트로 남음)

# list_all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "korea", 0]
# print(list_all)
# print(list_all.pop(11)) # 해당 인덱스의 값을 보여주고 삭제
# print(list_all.pop())   # 인덱스가 없으면 마지막 인덱스의 값을 보여주고 삭제

# del list_all[3]           # 해당 인덱스의 값을 삭제
# print(list_all)
#
# list_all.remove(0)        # 해당 인덱스의 값을 보여주지 않고 삭제
# print(list_all)
#
# list_all.clear()
# print(list_all)

# # 중복 제거
# my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,1,2,3,4]
# new_list = []
# for e in my_list:
#     if e not in new_list:
#         new_list.append(e)
# print(new_list)


# map(반환 함수, 입력 자료형), filter(반환 함수, 입력 자료형) 동작 확인
# num = list(filter(lambda e: int(e) % 2 == 0, input("값 : ").split()))
# print(num)

# 리스트의 원소 스캔하기
x = ["Jhon", "George", "Paul", "Ringo"]
for e in x:     # 향상된 for문과 비슷한 형태
    print(e)

for i in range(len(x)):     # 범위 기반 for문 (초기값, 최종값, 증감값)
    print(x[i])