# 첫째 줄에는 테스트 케이스의 개수 C
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수 나열

# 입력(ex)
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# 출력
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%

def over_rate():  # 각 케이스에서 평균이 넘는 비율 구하기
    score = list(map(int, input().split())) # 공백 기준으로 입력 받아 정수형 리스트로 담음
    average = sum(score[1:]) / len(score[1:]) # 공백 기준으로 맨 앞의 요소는 인원수이므로 제외
    cnt = 0  # 평균이 넘는 %를 구하기 위해서는 인원에 대한 카운트가 필요함.
    for i in range(1, len(score)):  # 맨 앞의 요소는 인원 수이므로 제외
        if score[i] > average: cnt+=1
    return cnt / (len(score)-1) * 100  # 백분율 표기로 변경

n = int(input())    # 총 테스트 횟수
rst = []  # 각 케이스에 대한 결과값을 받기 위한 리스트
for i in range(n): rst.append(over_rate())
for e in rst: print(f"{e:.3f}%")

