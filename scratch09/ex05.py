"""
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서
DataFrame으로 변환.
DataFrame의 행과 열의 개수 확인
DataFrame의 앞쪽 데이터 5개를 출력
DataFrame의 뒤쪽 데이터 5개를 출력
DataFrame의 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame에서 'country', 'lifeExp','gdpPercap' 컬럼들만 출력
DataFrame에서 행 인덱스가 0,99,999인 행들을 출력
DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력
DataFrame에서 연도(year)별 기대 수명의 평균을 출력
DataFrame에서 연도(year)별, 대륙(continent)별 기대 수명의 평균
"""
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep='\t')
# print(df)
print(df.shape)  # 행과 열의 개수 : (1704, 6)
print(df.head(5)) # 앞쪽 데이터 5개를 출력
print(df.tail(5)) # 뒤쪽 데이터 5개를 출력
print(df.dtypes) # 컬럼 이름들을 출력

cols = ['country','lifeExp','gdpPercap']
print(df[cols])
num =[0,99,999]
print(df.iloc[num]) # 행 인덱스가 0,99,999인 행들을 출력
cols2 = ['country','lifeExp','gdpPercap']
cols3 = [0,3,5]
print(df.iloc[840:851, cols3]) # 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력

group = df['lifeExp'].groupby(df['year']) # 연도(year)별 기대 수명의 평균을 출력
print(group.mean())

group1 = df['lifeExp'].groupby([df['year'],df['continent']]) # 연도(year)별, 대륙(continent)별 기대 수명의 평균
print(group1.mean())
