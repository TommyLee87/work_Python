# 딕셔너리를 사용해 학생의 인적사항 등록, 검색, 저장, 불러오기 기능 구현
# Rest API의 기본 형태인 JSON으로 저장 및 불러오기 (웹에서 API의 기본 포맷)
# 함수로 구현

import json  # 'JSON'형식으로 데이터를 저장하고 불러오기 위한 모듈
student_map = {}  # 학생 정보를 저장할 빈 딕셔너리 생성

# 학생 정보 등록
def reg_student():
    id = input("학번 : ")
    name = input("이름 : ")
    addr = input("주소 : ")
    student_map[id] = {"이름": name, "주소": addr}  # 값을 딕셔너리에 추가
    print(f"{name}님의 정보가 등록 되었습니다.")

def search_student():
    id = input("검색 할 학번 : ")
    info = student_map.get(id)  # get(key) 메서드로 학번을 얻어 옴
    if info :
        print(f"학번 : {id}")
        print(f"이름 : {info['이름']}")
        print(f"주소 : {info['주소']}")
    else:
        print("해당 학번의 학생 정보를 찾을 수 없습니다.")

#학생 정보 변경
def modify_student():
    id = input("수정 할 학번 : ")
    info = student_map.get(id)  # 학번을 키로 만들어 해당하는 값을 불러오도록(이름과 주소로 구성된 딕셔너리)
    if info:
        name = input("새 이름 : ")
        addr = input("새 주소 : ")
        info['이름'] = name
        info['주소'] = addr
        print(f"{name}님의 정보가 수정되었습니다.")
    else:
        print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# 학생 정보 삭제
def del_student():
    id = input("삭게 할 학번 : ")
    if student_map.get(id):
        del student_map.get[id]  # 키로 딕셔너리 삭제
        print ("학생 정보가 삭제 되었습니다.")
    else:
        print("해당 학번의 학생 정보를 찾을 수 없습니다. ")

# 학생 정보 보기
def view_all_student():
    for id in student_map:
        info = student_map[id]
        print(f"학번 : {id}")
        print(f"이름 : {info['이름']}")
        print(f"주소 : {info['주소']}")

def save_student():
    with open('student.json', 'w', encoding="utf-8") as file:
        json.dump(student_map, file, ensure_ascii=False)
        print("학생 정보가 저장 되었습니다.")

# JSON 파일을 불러 옴
def load_student():
    try:
        with open('student.json', 'r', encoding="utf-8") as file:
            student_map.clear()  # 현재 메모리에 있는 데이터 초기화
            student_map.update(json.load(file))
        print("학생 정보 파일을 열었습니다.")

    except FileNotFoundError:
        print("학생 정보 파일을 찾을 수 없습니다.")


while True:
    print("=" * 5, " 학생 정보 관리 프로그램 ", "=" * 5)
    choice = input("[1]등록 [2]검색 [3]수정 [4]삭제 [5]전체보기 [6]저장 [7]불러오기 [8]종료 : ")
    if choice == "1":
        reg_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        modify_student()
    elif choice == "4":
        del_student()
    elif choice == "5":
        view_all_student()
    elif choice == "6":
        save_student()
    elif choice == "7":
        load_student()
    elif choice == "8":
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택한 메뉴가 없습니다.")