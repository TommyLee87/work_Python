# 영단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로
# 단어의 길이는 최대 100자

rst = ""
for e in input() : # 입력받는 문자열만큼 자동 순회
    if e.islower():
        rst += e.upper()
    else:
        rst += e.lower()

print(rst)