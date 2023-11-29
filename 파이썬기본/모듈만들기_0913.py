# 모듈 : 코드가 저장된 파일
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱 : 처음부터 "." 인덱스 미만까지 -> naver 남음
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "LSU"
    return password

if __name__ == "__main__":   # 현재 파일이 엔트리포인트(진입지점) 인지 확인 할 때 사용
    print(add(1,4))
    print(sub(4,2))