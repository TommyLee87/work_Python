# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음.
# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함.

# # 큰 값과 작은값
# print(max(32, 45, 48, 57, 84))
# print(min(32, 45, 48, 57, 84))
#
# # 총 합 구하기
# print(sum([32, 45, 48, 57, 84]))   # 리스트에 대한 총 합
# print(sum((32, 45, 48, 57, 84)))   # 튜플에 대한 총 합
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 총 합 : {(sum(num)/len(num))}")
#
# # 몫과 나머지
# print(f"몫과 나머지 : {divmod (10, 4)}")   # 튜플의 동작 원리, 두 개의 반환 값을 받을 수 있음

# 여러 개의 값을 한 번에 입력 받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균

num = list(map(int, input("정수 입력 : ").split()))
print(f"최대값 : {max(num)}")
print(f"최소값 : {min(num)}")
print(f"합계 : {sum(num)}")
print(f"평균 : {sum(num) / len(num)}")
print(f" 몫과 나머지 : {divmod(sum(num), len(num))}")

# 정렬
my_list = [1, 2, 3, 44, 55, 5, 66, 7, 77, 888, 99, 999]
print(sorted(my_list))
print(sorted(my_list, reverse=True))
