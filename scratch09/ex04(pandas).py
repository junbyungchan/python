"""
pandas 패키지를 사용한 csv 파일 읽기
"""
import os

import matplotlib.pyplot as plt
import pandas as pd

file_path = os.path.join('..','scratch08','mpg1.csv')
df = pd.read_csv(file_path)
# 데이터 프레임의 앞의 일부분 데이터 출력
print(df.head(3)) # 데이터프레임.head() ---> 상위 (기본값:5)  n 개의 데이터를 보여줌
print('shape:', df.shape) # shape: (234, 11) 관츤값: 234, 변수: 11
print('data types:', df.dtypes) # data types:
                                # manufacturer     object
                                # model            object
                                # displ           float64
                                # year              int64
                                # cyl               int64
                                # trans            object
                                # drv              object
                                # cty               int64
                                # hwy               int64
                                # fl               object
                                # class            object
                                # dtype: object
# DataFrame.dtypes : 각 컬럼(변수)의 데이터 타입
# pandas의 데이터 타입: object(문자열), float(실수) , int(정수)
print(df.describe()) #*****기술 통계 요약 통계량***** 결과 창
#             displ         year         cyl         cty         hwy
# count  234.000000   234.000000  234.000000  234.000000  234.000000
# mean     3.471795  2003.500000    5.888889   16.858974   23.440171
# std      1.291959     4.509646    1.611534    4.255946    5.954643
# min      1.600000  1999.000000    4.000000    9.000000   12.000000
# 25%      2.400000  1999.000000    4.000000   14.000000   18.000000
# 50%      3.300000  2003.500000    6.000000   17.000000   24.000000
# 75%      4.600000  2008.000000    8.000000   19.000000   27.000000
# max      7.000000  2008.000000    8.000000   35.000000   44.000000

# DataFrame 에서 특정 컬럼의 모든 데이터를 선택
displ = df['displ']
print(displ)
cty = df['cty']

plt.scatter(x=displ,y=cty)
# plt.show()

# DataFrame에서 행(row)을 선택할 때,
# df.iloc[행 번호(인덱스)], df.loc[행 레이블]
print(df.iloc[0])
print(df.iloc[0:3]) # row index 0이상 3 미만인 행 선택

# 데이터 프레임에서 여러개의 컬럼(변수)들을 선택
cols =['displ','cty','hwy'] # []: 리스트
print(df[cols]) # []: 인덱스 연산자

# 데이터 프레임에서 여러개의 행(관측값)과 컬럼(변수)들을 선택
# df.loc[row_labels, col_labes] : 행과 열의 레이블(이름)
# df.iloc[row_indices, col_indices] : 행과 열의 인덱스(숫자)
print(df.loc[0:3, cols])
print(df.iloc[0:3, 0:3])




