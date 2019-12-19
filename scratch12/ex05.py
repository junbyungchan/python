"""
Boston house prices dataset
"""
from sklearn import linear_model
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 보스턴 집값 데이터 세트 로딩
# 데이터 탐색 - 그래프
# 학습 세트/ 검증 세트 나눔
# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# 검증 세트를 사용해서 예측 -> 그래프
# Mean Square Error 계산
# R2-score 계산
from sklearn.preprocessing import PolynomialFeatures

datasets = load_boston()
X = datasets.data
y = datasets.target
print(X.shape) # (506,13)
features = datasets.feature_names # 컬럼 이름 추출 ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
print(features)
print(X[0],y[0])
print(y.shape)


fig , ax = plt.subplots(4,4)
for row in range(4):
    for col in range(4):
        axis = ax[row,col]
        idx = 4 * row + col
        if idx > 12:
            break
        x = X[:,idx]
        axis.scatter(x,y)
        axis.set_title(features[idx])
plt.show()

# 데이터 세트 나눔
X_train ,X_test , y_train, y_test = train_test_split(X,y , test_size=0.2)
# X_train = X[:-100,]
# X_test = X[-100:,]
# y_train = y[:-100,]
# y_test = y[-100:,]
# 컬럼 'RM' 만
rm_train = X_train[:,np.newaxis,5]
rm_test = X_test[:,np.newaxis,5]

regr = linear_model.LinearRegression()
regr.fit(rm_train,y_train)
y_pred = regr.predict(rm_test)
print('intercept :', regr.intercept_)
print('coefficients :', regr.coef_)
print('mean_squared_error:',mean_squared_error(y_test,y_pred)) # 숫자가 작을수록 예측을 잘한것
print('r2_score :',r2_score(y_test,y_pred)) # 0~1 1에 가까울 수록 좋다

plt.scatter(rm_test,y_test)
plt.plot(rm_test,y_pred,'ro-')
plt.title('boston , rm')
plt.show()

# 다중 회귀  전체

regr.fit(X_train,y_train)
y_pred1 = regr.predict(X_test)

print('intercept :', regr.intercept_)
print('coefficients :', regr.coef_)
print('mean_squared_error:',mean_squared_error(y_test,y_pred1)) # 숫자가 작을수록 예측을 잘한것
print('r2_score :',r2_score(y_test,y_pred1)) # 0~1 1에 가까울 수록 좋다






