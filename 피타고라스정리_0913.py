# 직각삼각형에서 빗변을 제외한 나머지 두 변의 길이를 각각 제곱해 더하면 빗변의 길이의 제곱과 같다.

rst = []
while True:
    tri = list(map(int, input().split()))
    tri.sort()

    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    elif tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
        rst.append("right")
    else:
        rst.append("wrong")

for i in rst:
        print(i)





