# 집합이란 ? 주로 중복 제거를 목적으로 사용
# 순서가 보장되지 않음
# mutable 특성을 가짐
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

# 중복 제거
s3 = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3])
print(s3)

# 합집합 : 한 곳에만 존재하면 포함, 중복은 제거
print(s1.union(s2))
print(s1 | s2)

# 교집합 : 두 곳 모두 존재해야 함, 중복은 제거
print(s1.intersection(s2))
print(s1 & s2)

# 차집합 : 앞에서 뒤를 빼고 남은 앞의 요소, 중복은 제거
print(s1.difference(s2))
print(s1 - s2)

import random
nums = set()
while True:
    num = random.randrange(1,46)
    nums.add(num)
    if len(nums) == 6:
        break
print(nums)