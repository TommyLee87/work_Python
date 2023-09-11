# 계좌 개설
def open_account(name):
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name  # 반환 값으로 이름을 전달

# 입금 함수
def deposit(input):  # 잔고와 입금액을 매개 변수로 전달 받음
    global balance
    balance += input
    print(f"{input} 이 입금 되었습니다. 잔액은 {balance} 입니다.")


# 출금 함수
def withdraw(output):
    global balance
    if balance >= output:
        balance -= output
        print(f"{output} 이 출금 되었습니다. 잔액은 {balance} 입니다.")
    else:
        print(f"출금이 되지 않았습니다. 현재 잔액은 {balance}입니다.")


balance = 0  # 외부에서 선언했지만 매개 변수로 전달하여 결과를 리턴받음.
name = open_account("곰도리")
deposit(1000)
withdraw(500)

print(f"{name}님의 잔액은 {balance} 입니다.")