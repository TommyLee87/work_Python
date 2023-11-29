# 파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야 함.
# 파일객체 = open("파일명","파일모드","인코딩")
# 파일명 : 파일경로 + 파일명(파일 경로를 입력하지 않으면 현재 위치에 저장)
# 파일모드 : r(읽기), w(쓰기), a(추가, 파일이 없으면 생성하고 추가, 있으면 파일의 마지막에 추가)
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 50", file=score_file)
# print("영어 : 90", file=score_file)
# score_file.write("국어 : 98" + "\n")
# score_file.write("과학 : 45" + "\n")
# score_file.close()

# 파일읽기
# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 해당 파일의 내용을 한 줄씩 읽고 문자열로 반환, 더 이상 내용이 없으면 None
# readlines() : 해당 파일의 모든 내용을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 리스트 반환

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()
# while True:
#     line = score_file.readline()   # 한 줄씩 읽음
#     if not line:  # 더 읽을 내용이 없으면 None으로 확인되고, None은 거짓으로 본다.
#         break
#     print(line, end="")  # 한 줄씩 읽고 출력하기 때문에 줄바꿈 문자까지 포함되어 있음.
# score_file.close()
#
# lines = score_file.readlines()  # 해당 파일의 모든 라인을 순서대로 읽고 리스트 생성
# for e in lines:
#     print(e, end="")
# print(lines)
# score_file.close()

# with 키워드 사용하기 : open() 이후에 자동으로 close를 호출해 주는 기능
# with open("score.txt", "r", encoding="utf-8") as score_file:
#     print(score_file.read())
#
# print("프로그램의 끝")
from datetime import datetime
# with open("password.txt", "w") as f:
#     file_name = "password.txt"
#     fd = open(file_name, "wt")
#
#     while True:
#         url = input("사이트 : ")
#         if url == 'exit': break
#         my_str = url.replace("http://", "")
#         my_str = my_str[:my_str.index(".")]  # 슬라이싱 : 처음부터 "." 인덱스 미만까지 -> naver 남음
#         password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "LSU"
#         #             nav               5                     0                      0                !     LSU
#         print("비밀번호 : " + password)
#         fd.write(password + "\n")

import pickle
# 객체를 직렬화하여 파일에 저장하기
# data = {"name": "곰돌이사육사", "age": 22, "addr": "서울시 강남구 역삼동"}
# with open("data.pickle", "wb") as file:
#     pickle.dump(data,file)

# 파일에서 객체를 역직렬화하여 복원하기
with open("data.pickle", "rb") as file:
    restored_data = pickle.load(file)

print(restored_data)