"""
선형 회귀
"""
from sklearn import linear_model
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

# X, y = load_diabetes(return_X_y=True)
# print(X[:5])
# print(X.shape) # (442, 10)

datasets = load_diabetes()
X = datasets.data
y = datasets.target
print(X.shape , y.shape) # (442, 10) (442,) ---> 442개의 데이터, 10개의 컬럼 /// 442개의 데이터, 1개의 컬럼
features = datasets.feature_names  # 컬럼의 이름을 출력해준다.
print(features)
print('X[0] =',X[0])
# 모든 특성(컬럼)들이 평균=0, 표준 편차 = 1 로 전처리가 되어 있는 데이터 세트.
print('y[0] =',y[0])

# 선형 회귀(linear regression)
# y = b + a * x
# y = b0 + b1 * x1 + b2 * x2 + ...

# 1개의 figure에 10개의 subplot를 그려서, 변수들과 당뇨병(y)의 대략적인 관계를 파악하기.
# y ~ age, y ~ sex, y ~ bmi, ...

X_transpose = [column for column in zip(*X)]
print(len(X_transpose))

fig, ax = plt.subplots(3, 4)
for row in range(3):
    for col in range(4):
        axis = ax[row, col]
        idx = 4 * row + col
        if idx > 9:
            break
        x = X[:, idx]
        axis.scatter(x, y)
        axis.set_title(features[idx])
plt.show()

# y = b + a * bmi : y와 bmi 간의 성형 관계식
bmi = X[:, np.newaxis, 2] # data에서 'bmi'컬럼만 선택
# scikit-learn의 linearRegression은  2차원 배열 형태의 훈련 데이터 세트만 사용하기 때문에
# np.newaxis를 사용해야 한다.

print('bmi.shpae:',bmi.shape) # (442,) --> 1차원 배열이라는 의미이다.
print('bmi[5] =',bmi[:5]) # bmi[5] = [[ 0.06169621]
                                    # [-0.05147406]
                                    # [ 0.04445121]
                                    # [-0.01159501]
                                    # [-0.03638469]]

# bmi를 학습(train) / 검증(test) 세트로 분리
bmi_train = bmi[:-40] # 400번 까지
bmi_test = bmi[-40:] # 마지막 40번까지만

# y를 학습(train) / 검증(test) 세트로 분리
y_train = y[:-40]
y_test = y[-40:]
# train_set를 모델로 넘겨야한다.
# 선형회귀모델 (linear regression model) 객체 생성
regr = linear_model.LinearRegression() # linear_model import 한 후에 .LinearRegression()

# train set를 학습시킨다.(fitting 시킨다.)
# y = b + a * bmi 선형 관계식에서 y 절편 b 와 기울기 a를 결정
regr.fit(bmi_train,y_train) # bmi_train 이 1차원 배열이므로 에러가 난다.
# linear regression은 무조건 2차원 형태의 배열을 받아야한다.
print('coefficients:', regr.coef_) # coefficients: [955.44001079] 기울기를 출력! 선형회귀 객체.coef_ --> 기울기

# 예측하기 // 검증세트로 테스트!
y_pred = regr.predict(bmi_test) # 예측 값들이다.

# 그래프 y_pred 와 y_test의 그래프를 그려서 비교해보자
plt.scatter(bmi_test,y_test) # 실제값
plt.plot(bmi_test,y_pred,'ro-') # 예측값
plt.title('Diabetes , bmi')
plt.show()
# 오차(잔차)의 제곱의 값의 평균이 최소화 되는 과정을 찾아가는 것 : 선형회귀

# y ~ s5 사이의 선형 관계식을 찾고 그래프를 그려보자.

s5 = X[:,np.newaxis,-2] # 2차원 배열 형태로 s5 컬럼을 선택
s5_train = s5[:-40] # train_set
s5_test = s5[-40:] # test_set
y_train = y[:-40] # y_train_set
y_test = y[-40:] # y_test_set

regr_s5 = linear_model.LinearRegression() # 객체 생성
regr_s5.fit(s5_train,y_train) # 학습 시키기
print('coefficient:',regr_s5.coef_) # coefficient: [899.53962949]  기울기 계산
y_s5_pred = regr_s5.predict(s5_test) # 예측 하기
# 그래프 그리기
plt.scatter(s5_test,y_test)
plt.plot(s5_test,y_s5_pred,'ro-')
plt.title('Diabetes , s5')
plt.xlabel('s5')
plt.show()

arrary = np.array([[1,2],
                   [3,4]])
print(arrary) # 2x2 행렬(2차원 배열)
for row in range(2):
    for col in range(2):
        print(arrary[row,col],end=' ')
print()

arrary_flatten = arrary.flatten() # 2차원 배열을 1차원 배열로 펼쳐준다. ---> n차원 배열을 n-1 차원 배열로 만들어주는 메소드
print(arrary_flatten)
for i in range(4):
    print(arrary_flatten[i],end=' ')
print()


# flatten() 을 이용해서 subplot 다시 만들기
fig , ax = plt.subplots(3,4)
# ax : 3x4 형태의 2차원 배열
ax_flat = ax.flatten()
for i in range(len(features)):
    subplot = ax_flat[i]
    subplot.scatter(X[:,i],y)
    subplot.set_title(features[i])
plt.show()



