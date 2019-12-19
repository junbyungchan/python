"""
y = b + a * x : linear regression
y = b + a1 * x + a2 * x^2(다항식) -> 선형 회귀로 b, a1, a2를 결정할 수 있다.

y = b + a1 * x1 + a2 * x2 + ... : 선형 회귀
y = b + a1 * x1 + a2 * x2 + a3 * x1^2 + a4 * x1 * x2 + a5 * x2^2 --> 변수 5개 짜리 데이터 프레임이라고 생각하자!
--> 다중 선형 회귀와 비슷하게 생각하면 된다. x1, x2 옆에 컬럼에 추가된다고 생각하면 될것이다.
"""
import numpy as np
import sklearn.linear_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(1216)
# Training Set - data
X = 6 * np.random.rand(100,1) - 3 # X의 범위를  -3 <= x < 3
print('X =',X[:5])

# target
y = 0.5 + 2 * X + X**2 + np.random.randn(100,1) # np.random.randn(100,1) --> 에러항 --> 일부러 오차를 주기위해서 생성

A = np.array([[1],[2],[3]]) # 3 x 1 행렬 ( 2차원 리스트)
print('A =',A)
poly_feature = PolynomialFeatures(degree= 2, include_bias=False) # degree = n --> n차항을 만들겠다. , include_bias = False 상수항 생성 여부
# poly_feature.fit(A)
A_poly = poly_feature.fit_transform(A) # x ^2 컬럼이 추가됨
print('A_poly =',A_poly)

B = np.array([[1,2],[3,4]]) # 2x2 행렬(2차원 리스트)
print('B =',B)
poly_feature = PolynomialFeatures(degree=2, include_bias=False)
B_poly = poly_feature.fit_transform(B) # x1 ^2 , x1 * x2 , x2 ^ 2 컬럼이 추가됨
print('B_poly =',B_poly)
# 결과값 : B_poly = [[ 1.  2.  1.  2.  4.]
#                    [ 3.  4.  9. 12. 16.]]   # 순서: x1 , x2 , x1 ^ 2 , x1 * x2 , x2 ^ 2

X_poly = poly_feature.fit_transform(X) # 하나는 x의 항, 그리고 새로 생성된 x ^2의 항
print('X_poly =',X_poly)

lin_reg = LinearRegression()
lin_reg.fit(X_poly,y)
print('y 절편(intercept) :',lin_reg.intercept_) # y 절편(intercept) : [0.53611387]  실제 값 [0.5]
print('계수 (coefficients) :',lin_reg.coef_) # 계수 (coefficients) : [[2.02456163 0.97973891]] 실제 값 [[2,1]]
# y = b + a1 * x + a2 * x^2

X_test = np.linspace(-3,3,100).reshape(100,1) # -3 ~ 3 까지의 구간을 똑같은 크기로 100개로 나누겠다.
print(X_test[:5])
print(X_test[-5:])
X_test_poly = poly_feature.fit_transform(X_test)
y_pred = lin_reg.predict(X_test_poly)

plt.scatter(X,y)
plt.plot(X_test,y_pred,'r')
plt.show()







