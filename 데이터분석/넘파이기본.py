


# [] : 리스트
# {} : 딕셔너리
# () : 튜플
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 리스트로 데이터 생성

a1 = np.array(data) # 리스트를 넘파이 배열로 변환
print(a1)

data2 = [0, 1, 2, 3, 4, 5, 1.56, 3.14, 0.3333]
a2 = np.array(data2)
print(a2)

x = np.array([0.1, 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 배열 요소의 타입 확인

y = np.array(([1, 2, 3],[4, 5, 6]))
print(y)
print(y.shape) # 배열의 형태를 나타냄
print(y.dtype) # 배열 요소의 타입 확인

# 범위를 지정해 배열 생성
a3 = np.arange(0, 10, 2) # 0 ~ 10 미만, 간격은 2
print(a3)

a4 = np.arange(1, 20) # 1 ~ 20미만, 간격 생략 = 1
print(a4)

# 배열 형태 변환, 0 ~ 12미만 배열 생성
a5 = np.arange(12).reshape(4, 3) # 배열의 구조를 변경
print(a5)
print(a5.shape)

# 배열의 시작과 끝 지정, 그리고 데이터의 개수를 지정해 배열 생성
a6 = np.linspace(1, 10, 4) # 시작, 끝, 개수를 지정하면 시작과 끝 범위 내에서 값이 적절히 분포(배치)됨
print(a6)
a7 = np.linspace(0, np.pi, 20)
print(a7)

# 특별한 형태의 배열 생성
# 1차원 배열
a8 = np.zeros(10) # 0으로 채워진 10개 배열 생성
print(a8)
a9 = np.zeros((3, 4))
print(a9)
a10 = np.ones(10)
print(a10)
a11 = np.ones((5, 5))
print(a11)

# 단위 행렬 생성 : n x n 정사각형의 행렬에서 주 대각선이 모두 1
a12 = np.eye(4)
print(a12)

# 배열의 타입 변환 : 배열은 숫자 뿐만아니라 문자열도 요소로 가질 수 있음.(단, 같은 타입이어야 함)
a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592', '-12', '+12'])
print(a13)
print(a13.dtype) # <U8 의미 : 데이터 형식이 유니코드이며 문자의 최대 개수는 8개라는 의미
num_a13 = a13.astype(float) # 문자열을 실수 타입으로 변환
print(num_a13)

# 난수 배열의 생성 : 0 ~ 1 미만의 임의의 실수로 난수를 발생 시킴
a14 =  np.random.rand(2, 3)
print(a14)
print("")
a15 =  np.random.rand(2, 3, 4) # 3차원 배열
print(a15)

# 지정한 범위에 해당하는 정수로 난수 배열 생성
a16 = np.random.randint(10, size=(3, 10)) # 0 ~ 10미만의 정수
print(a16)

# 배열의 연산 : 넘파이(numpy)의 배열은 배열의 형태가 같다면 사칙연산 수행이 가능
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result= arr1 ** arr2
print(result)

# 요소별 연산 : True, False로 반환
arr3 = np.array([10, 20, 30, 40, 50])
print(arr3 > 20)

# 통계를 위한 연산 : 배열의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적동 등의 통계에서 많이 사용되는 메소드.
arr4 = np.arange(5) # 0 ~ 5미만의 값으로 구성된 배열 생성
print(f"합계 : {arr4.sum()}")
print(f"평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최대값 : {arr4.max()}")

# 배열 인덱싱
arr5 = np.arange(1, 6)
print(arr5[3])
print(arr5[0])
# 슬라이싱
new_arr = arr5[1:3] # 1번 인덱스에서 3번 인덱스 미만의 값을 새로운 배열로.
print(new_arr)

# Universal 함수 : 배열이 원소별 연산을 지원하는 함수
# 산술연산 : add(), substract(), multiply(), divide(), power()
# 삼각함수 : sin(), cos(), tan()
# 지수와 로그 : exp(), log(), log10()
# 집계함수 : sum(), min(), max(), mean()
# 논리함수 : logical_and(), logical_or(), logical_not()

xx = np.arange(0., 2*np.pi, 0.1)
yy = np.sin(xx)
print(yy)

matrix1 = np.array([[1,2], [4,5]])
matrix2 = np.array([[5,6], [7,8]])
# 행렬 덧셈
res = np.add(matrix1, matrix2)
print(res)
# 정렬과 탐색 : 배열의 정렬과 탐색을 위한 함수와 메소드
xxx = np.array([9, 8, 7, 2, 3, 4, 6, 11])
print(np.amin(xxx)) # 배열 내의 최소값
print(np.amax(xxx)) # 배열 내의 최대값
print(np.argmin(xxx)) # 배열내의 최소값의 위치
print(np.sort(xxx)) # 오름차순
print(np.sort(xxx)[::-1]) # 내림차순
print(np.argsort(xxx)) # 값의 인덱스

# 브로드캐스팅 : 배열의 크기가 다른 경우에 연산을 수행하도록 해주는 기능
ax = np.array([1, 2, 3]) # 1차원 배열
bx = np.array([[4], [5], [6]]) # 2차원 배열 (3 x 1)

cx = ax + bx
print(cx)
