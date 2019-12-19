import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(1216)
X = 2 * np.random.rand(100, 1)
print('X.shape:' , X.shape) # 2x1 행렬(2차원 ndarray), 데이터 : 0.0~ 2.0 사이의 숫자들로 이루어진 100x1 행렬(2차원 ndarray)

y = 4 + 3 * X + np.random.randn(100,1)
print('y.shape:',y.shape)

plt.scatter(X,y)
plt.show()

X_b = np.c_[np.ones((100,1)),X] # X의 행렬 앞에 1을 모두 붙여준것.
print('X_b.shape:', X_b.shape)
print(X_b[:5])

# linalg 모듈 : Linear Algebra(선형 대수)
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y) # inv() --> inverse 역행렬 , T --> Transpose  행과 열을 바꿔준다.
# dot()의 의미 : 내접
print(theta_best) # [[3.90187826] # b : y절편
                  # [3.07247138]] # a : 기울기

# 행렬식을 이용해서 찾은 theta 값과 LinearRegression 클래스에서 계산된 theta와 비교
lin_reg = LinearRegression()
lin_reg.fit(X,y)
print(f'y절편 : {lin_reg.intercept_}, 기울기 : {lin_reg.coef_}') # y절편 : [3.90187826], 기울기 : [[3.07247138]]

X_test = [[0],
          [1],
          [2]]
# 행렬식 : y = X_b * theta    ===> 행렬 X에 왼쪽 첫번쨰 컬럼에 1을 모두 삽입해야한다.
X_test_b = np.c_[np.ones((3,1)),X_test] # 행렬 X에 모든 숫자가 1인 컬럼을 추가한다.
print(X_test_b)
y_pred = X_test_b.dot(theta_best)
print(y_pred)

# scikit-learn 패키지를 사용한 예측
predictions = lin_reg.predict(X_test)
print(predictions) # 위의 행렬식과 똑같은 원리로 작동한다.

plt.scatter(X,y)
plt.plot(X_test,y_pred,'ro-')
plt.show()





