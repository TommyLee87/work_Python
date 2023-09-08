# 영식 요금제 : 30초마다 10원씩 청구, 30초부터 59초 사이로 통화를 했으면 20원이 청구
# 민식 요금제 :  60초마다 15원씩 청구, 60초부터 119초 사이로 통화를 했으면 30원이 청구
# 동호는 어디 가입할래 ?
# 동호 통화 수 : N <= 20
# 통화 시간 : N <= 10,000

n = int(input("통화 횟수 : "))   # 통화 횟수
call = list(map(int, input("통화당 시간 : ").split()))          # 통화 횟수에 대한 통화 시간
y_pay = m_pay = 0
for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10  # 전화 1통 : 10원 + 30초당 10원
    m_pay += (call[i] // 60) * 15 + 15  # 전화 1통 : 15원 + 60초당 15원

if y_pay > m_pay:
    print("M",m_pay)
elif y_pay < m_pay:
    print("Y", y_pay)
else:
    print("Y,M", y_pay)