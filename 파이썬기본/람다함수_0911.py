# 람다란 ? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 파이썬에서 람다 함수를 통해 이름이 없는 함수를 만들 수 있음
# 람다 함수의 장점은 코드의 간결함, 메모리의 절약


# def add(a,b):
#     return a + b
# print(add(1,2))
#
# print((lambda a,b:a+b)(1,2))

# 함수의 매개 변수로 함수 전달하기
# def call_times(func):
#     for i in range(10):
#         func()
# def print_hello():
#     print(f"hello^^ ")
#
# call_times(print_hello)

# filter() 함수와 map() 함수

# filter(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴값이 True인 것으로 새로운 리스트를 구성
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 새로운 리스트를 구성해주는 함수

def power(n):
    return n * n

power_l = lambda n: n * n   # 람다 식ㅇ로 구현하여 변수에 대입하는 방법

in_ = [1, 2, 3, 4, 5]

out_ = list(map(lambda n:n * n, in_))   # 함수 자리에 람다식으로 임의의 함수를 만들어 넣는 방법
print(out_)

# 리스트에 람다 함수를 넣는 방법도 가능
my_list = [lambda a,b: a * b, lambda a, b: a + b]
print(my_list[0](5,2))
print(my_list[0](5,2))