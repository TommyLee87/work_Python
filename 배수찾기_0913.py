# 첫째 줄에 n(0 < n < 1000)
# 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성

n = int(input())
ls = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        ls.append(a)

for i in range(len(ls)):
    if ls[i] % n == 0:
        print(f"{ls[i]} is a multiple of {n}.")
    else:
        print(f"{ls[i]} is not a multiple of {n}.")







