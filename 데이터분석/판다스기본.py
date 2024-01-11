import pandas as pd
import numpy as np

# 판다스 : 데이터 분석과 조작을 위한 라이브러리, 데이터를 구조화하고, 저장, 처리, 분석을 수행

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
print(s1.index)
print(s1.values)

# 판다스는 요소의 데이터 타입이 달라도 가능
s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print(s2)

# 데이터가 없는 경우 넘파이 np.nan으로 표시 가능
s3 = pd.Series([np.nan, 10, 30])
print(s3)

# Series 데이터 생성 시 인덱스 추가 기능
index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 345], index=index_date)
print(s4)

# 파이썬의 딕셔너리 이용
s5 = pd.Series({'국어' : 100, '영어' : 95, '수학' : 90})
print(s5)

# 날짜 자동 생성
s6 = pd.date_range(start='2023-09-16', end='2023-10-10')
print(s6)

# 달력을 요일 기준으로 일주일씩 증가
s7 = pd.date_range(start='2023-09-16', periods=4, freq='W')
print(s7)

# 데이터프레임 : 데이터를 다룰 때 가장 많이 사용하는 데이터 형태로, 행과 열로 구성된 사각형 모양의 표
df = pd.DataFrame({'name' : ['민지', '하니', '혜린', '다니엘', '혜인'],
                   'kor' : [90, 88, 97, 77, 92],
                   'eng' : [88, 92, 87, 96, 97]
                   })
print(df)
print(df['kor'])
print(sum(df['kor'])/df['kor'].size) # 평균 구하기

# 실습문제
df_fruit = pd.DataFrame({
    '제품' : ['사과', '딸기', '수박'],
    '가격' : [1800, 1500, 3000],
    '판매량' : [24, 38, 13]
})

print(f"과일 평균 가격 : {sum(df_fruit['가격']) / df_fruit['가격'].size}")
print(f"평균 판매량 : {sum(df_fruit['판매량']) / df_fruit['판매량'].size}")

# 엑셀파일 읽기
df_excel = pd.read_excel('./excel_exam.xlsx')
print(df_excel)

print(f"엑셀의 영어 평균 점수 : {sum(df_excel['english']) / df_excel['english'].size}")
print(f"엑셀의 수학 평균 점수 : {sum(df_excel['math']) / df_excel['math'].size}")
print(f"엑셀의 과학 평균 점수 : {sum(df_excel['science']) / df_excel['science'].size}")

# CSV(Comma Seperated Values) 파일 읽기
df_csv = pd.read_csv('./exam.csv')
print(df_csv)

# 데이터프레임을 CSV 파일로 저장하기
df_fruit.to_csv('과일데이터프레임.csv', index=False)

# head() : 데이터 앞부분 확인하기
exam = pd.read_csv('./exam.csv')
print(exam.head(10))

# tail() : 데이터 뒷부분 확인하기
exam = pd.read_csv('./exam.csv')
print(exam.tail(10))

# info() : 변수 속성 파악하기
print(exam.info())

# describe() : 요약 통계량 구하기
print(exam.describe())

# mgp 데이터 파악하기
mpg = pd.read_csv('./mpg.csv')
print(mpg.head())
print(mpg.tail())
print(mpg.shape)
print(mpg.info())
print(mpg.describe())
print(mpg.describe(include='all'))

# 패키지 함수
pd.read_csv('./exam.csv')
pd.DataFrame({'x' : [1,2,3]})

# 매서드
print(df.head())
print(df.info())

# 어트리뷰트
print(df.shape)

# 변수명 바꾸기 : pandas의 df.rename()을 이용해 변수명을 바꾸는 방법
# 데이터 프레임 만들기
df_raw = pd.DataFrame({
  'var1' : [1, 2, 1],
  'var2' : [2, 3, 2]
})
print(df_raw)

# 복사본 만들기
df_new = df_raw.copy()
print(df_new)

# 변수명 바꾸기
df_new = df_new.rename(columns={'var2' : 'v2'})
print(df_new)

# 실습문제
mpg = pd.read_csv('./mpg.csv')
mpg_new = mpg.copy() # 복사본
mpg_new = mpg_new.rename(columns={'cty' : 'city',
                                  'hwy' :'highway'})  # 변수면 변경
print(mpg_new.head())

# 파생변수 만들기
df = pd.DataFrame({
  'var1' : [4, 3, 8],
  'var2' : [2, 6, 1]
})
print(df)
df['var_sum'] = df['var1'] + df['var2'] # 파생 변수 만들기
df['var_mean'] = (df['var1'] + df['var2']) / 2
print(df)

# mpg 통합 연비 변수 만들기
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
print(mpg.head())
print(sum(mpg['total']) / len(mpg))
print(mpg['total'].mean()) # 위 보다 간단하게 mean 사용

# 조건문을 활용해 파생변수 만들기
# 기준값 정하기
print(mpg['total'].describe()) # 요약 통계량 출력
print(mpg['total'].plot.hist())

# 합격 판정 변수 만들기
mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
print(mpg.head())

print(mpg['test'].value_counts()) # 연비 합격 빈도표 만들기

count_test = mpg['test'].value_counts() # 연비 합격 막대 그래프 만들기
print(count_test.plot.bar()) # 축 이름 회전하기

# 중첩 조건문 활용하기 : 범주 값을 3가지 이상으로 부여하려면 np.where()안에 다시 np.where()를 넣는 형식.
# 연비 등급 변수 만들기
# total 기준으로 A, B, C 등급 부여
mpg['grade'] = np.where(mpg['total'] >= 30, 'A',
                  np.where(mpg['total'] >= 20, 'B', 'C'))
# 데이터 확인
print(mpg.head())

# 등급 빈도표 만들기
count_grade = mpg['grade'].value_counts()
print(count_grade)
print(count_grade.plot.bar(rot=0))

# 알파벳순으로 막대 정렬하기 : df.value_counts()에 sort_index()를 추가
count_grade = mpg['grade'].value_counts().sort_index()
print(count_grade)

# 목록에 해당하는 행으로 변수 만들기
mpg['size'] = np.where((mpg['category'] == 'compact') |
                       (mpg['category'] == 'subcompact') |
                       (mpg['category'] == '2seater'),
                       'small', 'large')
print(mpg['size'].value_counts())

# 조건이 여러 번 반복 될 때 df.isin()을 사용
mpg['size'] = np.where(mpg['category'].isin(['compact', 'subcompact', '2seater']), 'small', 'large')
print(mpg['size'].value_counts())

# 실습문제
# 1. midwest.csv를 불러와 데이터의 특징을 파악
midwest = pd.read_csv('./midwest.csv')  # 데이터 불러오기
print(midwest.head())                        # 앞부분 출력
print(midwest.tail())                        # 뒷부분 출력
print(midwest.shape)                         # 행, 열 개수 출력
print(midwest.info())                       # 변수 속성 출력
print(midwest.describe())                    # 요약 통계량 출력

# 2. poptotal(전체 인구) 변수를 total로, popasian(아시아 인구) 변수를 asian으로 수정
midwest = midwest.rename(columns = {'poptotal' : 'total'}) # poptotal을 total로 수정
midwest = midwest.rename(columns = {'popasian' : 'asian'}) # popasian을 asian으로 수정
print(midwest['total'])
print(midwest['asian'])

# 3. total, asian 변수를 이용해 ‘전체 인구 대비 아시아 인구 백분율’ 파생변수를 추가하고, 히스토그램 만들기
midwest['ratio'] = midwest['asian'] / midwest['total'] * 100 # 백분율 변수 추가
print(midwest['ratio'])
print(midwest['ratio'].plot.hist()) # 히스토그램 만들기

# 4. 아시아 인구 백분율 전체 평균을 구하고, 평균을 초과하면 'large', 그 외에는 'small'을 부여한 파생변수 만들기
print(midwest['ratio'].mean()) # ratio 평균
midwest['group'] = np.where(midwest['ratio'] > 0.4872, 'large', 'samall') # large, samll 부여
print(midwest['group'])

# 5. 'large'와 'small'에 해당하는 지역이 얼마나 많은지 빈도표와 빈도 막대 그래프를 만들기
print(midwest['group'].value_counts().plot.bar(rot = 0))
