# 1. 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력

# num = list(map(int, input("무작위 숫자 입력 : ").split()))
#
# list_odd = []
# list_even = []
#
# for e in num:
#     if e % 2 == 0:
#         list_even.append(e)
#     else:
#         list_odd.append(e)
# print(f"홀수 : {list_odd}")
# print(f"짝수 : {list_even}")

# map : 전달 받은 갯수를 함수 내부에서 가공해서 반환 (입력 개수와 반환 개수가 동일)
# filter : 전달 받은 갯수를 함수 내부에서 조건에 부합하는 것만 반환

# 2. 람다식으로 풀기
num = list(map(int, input("무작위 숫자 입력 : ").split()))
list_odd = list(filter(lambda e: int(e) % 2 != 0, num))
list_even = list(filter(lambda e: int(e) % 2 == 0, num))

print(f"홀수 : {list_odd}")
print(f"짝수 : {list_even}")
