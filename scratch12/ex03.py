"""
y = b + a1 * x1 : 단순 선형 회귀
y = b + a1 * x1 + a2 * x2 + ... : 다중 선형 회귀
"""
import numpy as np

# 가상의 데이터 만들기
from sklearn.linear_model import LinearRegression

np.random.seed(1216)
X1 = np.random.rand(100,1)
print('x1 :',X1[:5])
X2 = np.random.rand(100,1)
print('x2 :',X2[:5])

y = 3 + 4 * X1 + 5 * X2 + np.random.randn(100,1) # target
print('y :',y[:5])

# X1 과 X2 가 쪼개져 있으므로 합친다.
X = np.c_[X1,X2] # data
print('X :',X[:5])

lin_reg = LinearRegression() # LR 객체 생성
lin_reg.fit(X,y) # 학습시키기 /// model fitting, 학습
# 절편 출력
print('y 절편(intercept): ',lin_reg.intercept_) # y 절편:  [2.66850283]
# 계수들 출력
print('계수(coefficients): ',lin_reg.coef_) # 계수:  [[4.56940359 5.1255058 ]] /// 값이 2개인 이유는 a1, a2에 대한 값이 필요하므로




