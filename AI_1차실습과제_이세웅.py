import random
yut=['xxxx','xxxo','xxox','xxoo','xoxx','xoxo','xoox','xooo','oxxx','oxxo','oxox','oxoo','ooxx','ooxo','ooox','oooo' ]
throw = random.choice(yut)
print(throw)
n = throw.count('o')
if n == 4:
    print("모")
elif n == 3:
    print("도")
elif n == 2:
    print("개")
elif n == 1:
    print("도")
elif n == 0:
    print("윷")