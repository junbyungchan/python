"""
Boston house prices dataset
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 보스턴 집값 데이터 세트 로딩
dataset = load_boston()  # Bunch: 파이썬의 dict와 비슷한 타입
print(type(dataset))
print(dataset.keys())
print(dataset['DESCR'])  # dataset.DESCR

# 데이터와 타겟을 구분
X = dataset['data']  # dataset.data
y = dataset['target']  # dataset.target
print('X shape:', X.shape)  # (506, 13)
print(X[:2])
print('y shape:', y.shape)  # (506,)
print(y[:2])

features = dataset['feature_names']  # dataset.feature_names
print(features)

# 데이터 탐색 -> y ~ feature 산점도 그래프
fig, ax = plt.subplots(4, 4)  # 16개의 subplot을 생성
ax_flat = ax.flatten()
for i in range(len(features)):  # 특성(변수)들의 개수만큼 반복
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)  # y ~ feature 산점도 그래프
    axis.set_title(features[i])  # subplot에 타이틀 추가
plt.show()

# 학습 세트/검증 세트 나눔
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(f'X_train len: {len(X_train)}, X_test len: {len(X_test)}')

# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# price = b0 + b1 * rm: 주택 가격 ~ 방의 개수(rm)
X_train_rm = X_train[:, np.newaxis, 5]  # 2차원 배열
X_test_rm = X_test[:, np.newaxis, 5]
print(f'X_train_rm: {X_train_rm.shape}, X_test_rm: {X_test_rm.shape}')

lin_reg = LinearRegression()  # Linear Regression 객체 생성
lin_reg.fit(X_train_rm, y_train)  # fit(적합)/학습(training) -> b0, b1 찾음
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

# 검증 세트를 사용해서 예측 -> 그래프
y_pred_rm = lin_reg.predict(X_test_rm)

# 실제값(scatter), 예측값(plot) 그래프
plt.scatter(X_test_rm, y_test)
plt.plot(X_test_rm, y_pred_rm, 'r')
plt.title('Price ~ RM')
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()

# MSE(Mean Squared Error: 오차 제곱들의 평균) 계산
# error = y - y_hat, error^2 = (y - y_hat)^2
# MSE = sum(error^2) / 개수
mse = mean_squared_error(y_test, y_pred_rm)
# RMSE(Squared-Root MSE)
rmse = np.sqrt(mse) # mse 숫자가 너무 커서 root를 씌워서 숫자를 줄였다.
print('Price ~ RM: RMSE =', rmse)

# R2-score(결정 계수) 계산
r2_1 = lin_reg.score(X_test_rm, y_test) # 아래식과 같다.
r2_2 = r2_score(y_test, y_pred_rm)
print(f'Price ~ RM: R^2 = {r2_1}, {r2_2}')

# Price ~ LSTAT 선형 회귀: price = b0 + b1 * lstat
X_train_lstat = X_train[:, np.newaxis, 12]  # 학습 세트
X_test_lstat = X_test[:, np.newaxis, 12]  # 검증 세트

lin_reg.fit(X_train_lstat, y_train)  # 모델 fit, train
print(f'Price ~ LSTAT: intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat = lin_reg.predict(X_test_lstat)  # 예측, 테스트

plt.scatter(X_test_lstat, y_test)  # 실제값 산점도 그래프
plt.plot(X_test_lstat, y_pred_lstat, 'r')  # 예측값 선 그래프
plt.title('Price ~ LSTAT')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat)
rmse = np.sqrt(mse)
r2 = lin_reg.score(X_test_lstat, y_test)
# r2_score(y_test, y_pred_lstat)
print(f'Price ~ LSTAT: RMSE = {rmse}, R^2 = {r2}')

# Price ~ LSTAT + LSTAT^2 선형 회귀
# price = b0 + b1 * lstat + b2 * lstat^2
poly = PolynomialFeatures(degree=2, include_bias=False)   # ======================================poly
# 데이터에 다항식 항들을 컬럼으로 추가해 주는 클래스 객체
# 학습 세트에 다항식 항을 추가 -> fit/train할 때 사용
X_train_lstat_poly = poly.fit_transform(X_train_lstat)
# 검증 세트에 다항식 항을 추가 -> predict/test할 때 사용
X_test_lstat_poly = poly.fit_transform(X_test_lstat)

lin_reg.fit(X_train_lstat_poly, y_train)  # fit/train
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat_poly = lin_reg.predict(X_test_lstat_poly)  # predict/test

plt.scatter(X_test_lstat, y_test)  # 실제값
xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100, 1))
xs_poly = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')
plt.title('Price ~ lstat + lstat^2')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat_poly)  # 오차 제곱 평균
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_lstat_poly)  # 결정 계수
# lin_reg.score(X_test_lstat_poly, y_test)
print(f'Price ~ LSTAT^2: RMSE = {rmse}, R^2 = {r2}')

# Price ~ RM + LSTAT 선형 회귀: price = b0 + b1 * rm + b2 * lstat
X_train_rm_lstat = X_train[:, [5, 12]] # RM , LSTAT 의 컬럼을 뽑아내기 X_train_rm_lstat = X_train[ : , [5 , 12]]
X_test_rm_lstat = X_test[:, [5, 12]]
print(X_train_rm_lstat[:5])

lin_reg.fit(X_train_rm_lstat, y_train)  # fit/train
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)  # predict/test
print('y_true', y_test[:5])
print('y_pred', y_pred_rm_lstat[:5])

mse = mean_squared_error(y_test, y_pred_rm_lstat)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat)
print(f'Price ~ RM + LSTAT: RMSE = {rmse}, R^2 = {r2}')

# Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 * rm^2 + b4 * rm * lstat + b5 * lstat^2
# 학습 세트에 다항식항(컬럼)을 추가
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)
print(X_test_rm_lstat_poly[:2]) # 제대로 만들어 졌는지 확인
# [[  8.259      3.54      68.211081  29.23686   12.5316  ]
 # [  6.312     10.58      39.841344  66.78096  111.9364  ]]   출력 값 5개의 항은
 # rm / lstat / rm ^2 / rm*lstat / lstat^2

lin_reg.fit(X_train_rm_lstat_poly,y_train) # 모델을 훈련시키기 fit/train
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')
# intercept: 58.131040227957655 ----> b0값, coefficients: [-1.76285033e+01(rm의 계수)  1.52009093e+00(lstat의 계수)
# 2.09295492e+00(rm^2의 계수) -3.53889752e-01(rm * lstat 의 계수) -3.14275848e-03 (lstat ^2 의 계수)]
# 계수 : 5개 나와야한다.

# -1.76285033e+01(rm의 계수) rm은 원래 양의 관계였는데 다른 항들을 추가하다보니 음의 관계가 나왔다.
# 과적합?

y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly) # 예측 하기
print('y_true:' , y_test[:5]) # y_true: [42.8 21.2 31.  14.1 25.3]
print('y_predict', y_pred_rm_lstat_poly[:5].round(2)) # y_predict [50.3  22.34 28.86 16.01 25.07]

mse = mean_squared_error(y_test,y_pred_rm_lstat_poly)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred_rm_lstat_poly)
print(f'Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2 : RMSE = {rmse}, R^2 = {r2}')
# Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2 : RMSE = 5.715001544053191, R^2 = 0.6303959336867977

# Price ~ RM + LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 * lstat^2
X_train_last = np.c_[X_train_rm,X_train_lstat_poly] # 이미 모델이 있기 때문에 합쳐서 사용 가능하다.
X_test_last = np.c_[X_test_rm, X_test_lstat_poly]
print('X_train_last shape :', X_train_last.shape) # (354, 3)
print(X_train_last[:2]) #  [[  5.093   29.68   880.9024] [  6.251   16.44   270.2736]]
print('X_test_last shape :', X_test_last.shape) # (152, 3)
print(X_test_last[:2]) # [[  8.259    3.54    12.5316] [  6.312   10.58   111.9364]]
lin_reg.fit(X_train_last,y_train) # fit/train
print(f'Price ~ RM + LSTAT + LSTAT^2 : intercept: {lin_reg.intercept_}, coefficient: {lin_reg.coef_}')
# Price ~ RM + LSTAT + LSTAT^2 : intercept: 11.976646227033507, coefficient: [ 4.14148052 -1.79652146  0.03381396]

y_pred_last = lin_reg.predict(X_test_last) # 예측하기
print('y true:',y_test[:5]) # y true: [42.8 21.2 31.  14.1 25.3]
print('y predict:',y_pred_last[:5].round(2)) # y predict: [40.25 22.9  26.39 16.14 28.23]

mse = mean_squared_error(y_test,y_pred_last)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred_last)
print(f'Price ~ RM + LSTAT + LSTAT^2 : RMSE = {rmse} , R^2 = {r2}')
# Price ~ RM + LSTAT + LSTAT^2 : RMSE = 5.592903859241363 , R^2 = 0.6460199841225782





