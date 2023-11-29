# 고정비용 : 1000
# 가변비용 : 70
# 판매비용 : 170

# (1) : 보통 푸는 방식이지만 이렇게 풀면 안됨
# fix, var, sell = map(int, input().split())
# cnt = 0
# while True:
#     if fix + (var * cnt) < sell * cnt:
#         break
#     cnt += 1
# print(cnt)

# (2) : 풀이 1번
# fix, var, sell = map(int, input().split())
# cnt = 0
# while True:
#     if cnt > fix // (sell - var):
#         break
#     cnt += 1
#
# print(cnt)

# (3) : 손익분기점 공식
fix, var, sell = map(int, input().split())
if sell <= var:
    print(-1)
else:
    print(fix // (sell - var) + 1)
