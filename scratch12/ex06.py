"""
pip install seaborn 설치하기
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()
X = boston['data'] # boston.data
y = boston['target'] # boston.target
features = boston['feature_names'] # boston.feature_names

# numpy.ndarray 타입을 pandas.DataFrame 타입으로 변환
boston_df = pd.DataFrame(X, columns= features)
# 데이터프레임에는 target컬럼을 추가해야한다
boston_df['Price'] = y

print(boston_df.head())
print(boston_df.shape) # (506, 14)
# 통계 요약 정보
print(boston_df.describe())

columns = ['LSTAT', "INDUS",'NOX','RM','Price']
subset_df = boston_df[columns]
print(subset_df.head())

sns.pairplot(subset_df) # 각 5개의 변수 모두의 산관 그래프를 보여준다.
# subset_df 의 컬럼이 5개 이므로 5 x 5 = 25개가 나온다.
plt.show()

# 상관행렬(correlation matrix): 상관 계수들로 만든 행렬
# dataframe.corr() 상관계수를 계산해주는 함수
corr_matrix = subset_df.corr().round(2)

# heatmap : 상관 계수(correlation coefficient)들을 색상으로 표시한 그래프.
sns.heatmap(corr_matrix,annot=True) # annot = True 숫자도 같이 출력을 하겠다.
plt.show()








