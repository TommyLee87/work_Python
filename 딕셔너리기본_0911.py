# 딕셔너리 : 키와 값이 한쌍으로 이루어진 구조 (자바의 맵과 동일)
# 중괄호{} 감싸서 선언, 쉼표로 구분
# 키와 값은 콜론으로 구분

coffee_menu = {"Americano": 2500, "Espresso": 2500, "Latte": 4000, "Moca": 4500}
tea_menu = {"Black tea": 4000, "Green tea": 4000, "Milk tea": 3500}
food_menu = {"Cake": 5000, "Bakery": 6000, "Icecream": 7000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["Americano"])  # 키로 값 확인 하기
print(food_menu.get("Icecream"))  # get 함수로 값 확인 하기

# update 함수 : 딕셔너리의 데이터를 한꺼번에 변경
dict = {"곰탱이": 90, "안유진": 88, "장원영": 77}
dict.update({"곰탱이": 100, "장원영": 100})
print(dict)

# 정보 얻기 : kyes(), values(), items()
dict1 = {"Java": 80, "JavaScript": 88, "HTML": 70}
print(dict1.keys())  # 딕셔너리에 포함된 키만 확인
print(dict1.values())  # 딕셔너리에 포함된 값만 확인
print(dict1.items())  # 딕셔너리에 포함된 키와 값 확인

# 키의 포함 여부 확인
print("HTML" in dict1)  # 딕셔너리에 키가 포함되어 있는지 확인
print("Python" in dict1)
print(dict1.get("JavaScript"))

# 반복문에 키를 사용해 값을 가져오기
for key in coffee_menu:  # 딕셔너리를 for문으로 순회하면서 요소의 키 값을 자동으로 접근할 수 있음.
    print(key, " : ", coffee_menu[key])

