menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],  # 값을 리스트로 만들어 여러가지 정보를 포함
    "Espresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

while True:
    print("메뉴를 선택하세요 : ")
    menu = input("[1]메뉴 리스트 [2]메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]종료 : ")  # input은 문자열
    if menu == "1":
        for key in menu_dic:
            print(key, " : ", menu_dic[key])  # 딕셔너리에 키가 있는지 확인하는 질문

    elif menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력하세요 : ")
        if rtrv_name in menu_dic:
            print(menu_dic[rtrv_name])
        else:
            print("선택하신 메뉴는 존재하지 않습니다.")

    elif menu == "3":
        add_menu = input("추가 할 메뉴를 입력하세요 : ")
        if add_menu not in menu_dic:
            category = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("설명 : ")
            menu_dic[add_menu] = [category, price, desc]  # 추가 : 딕셔너리[키] = 값
            for key in menu_dic:  # 추가 된 메뉴 리스트를 보여준다
                print(key, " : ", menu_dic[key])
        else:
            print("이미 존재하는 메뉴입니다.")
        for key in menu_dic:  # 현재 메뉴 현황을 다시 보여준다
            print(key, " : ", menu_dic[key])

    elif menu == "4":
        del_menu = input("삭제 할 메뉴를 선택하세요 : ")
        if del_menu in menu_dic:
            del menu_dic[del_menu]  # 삭제 : del 딕셔너리[키]
            for key in menu_dic:
                print(key, " : ", menu_dic[key])
        else:
            print("존재하지 않는 메뉴입니다.")

    elif menu == "5":
        print("메뉴를 종료합니다.")
        break
    else:
        print("메뉴를 확인하시고 다시 선택해주세요.")

