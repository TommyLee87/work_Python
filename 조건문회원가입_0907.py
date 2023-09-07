# 회원 가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 8 : # 입력 받은 아이디의 길이가 8 이상.
    pw = input("비밀번호 입력 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16:  #내부 함수 이용
    if len(pw) < 8 or len(pw) > 16:   # 외부 함수 이용
        print("비밀번호는 8자 이상, 16자 미만으로 입력해주세요.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")

else:
    print("아이디는 반드시 8자 이상이어야 합니다.")