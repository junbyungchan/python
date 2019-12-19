"""
Linear Regression(선형 회귀): 값을 예측
Logistic Regression(로지스틱 회귀): 분류(classification)
"""

from sklearn import datasets
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression # logistic regression
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris['data'] # iris.data
y = iris['target'] # iris.target
features = iris['feature_names'] # iris.feature_names
print(features)

# 데이터 프레임 생성
iris_df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# 데이터 프레임에 컬럼(변수, 특성)을 추가
iris_df['species'] = y

print(iris_df.iloc[:5,:])
print(iris_df.describe())
sns.pairplot(iris_df, hue= 'species',
             vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
plt.show()

# 데이터(X) 와 타겟(y)을 학습/ 검증 세트로 분리
# 데이터가 랜덤하게 섞여있을 때에는 X[ : -100] / X[ -100: ] 이렇게 나눠도 된다.
# 하지만 정렬되있는 데이터들은 train_test_split을 이용해야한다.
X_train , X_test, y_train , y_test = train_test_split(X,y,test_size=0.2, random_state= 1217)
# random_state = seed랑 같은 의미

# 분류 알고리즘 중에서 Logistic Regression을 선택
log_reg = LogisticRegression() # 객체 생성

# 모델 적합(fitting)/ 학습(training)
log_reg.fit(X_train,y_train)

# 학습된 모델을 사용해 test_set을 분류 예측
predictions = log_reg.predict(X_test)
print('True=',y_test)
print('Predictions =',predictions)

# 성능 측정
print(confusion_matrix(y_test,predictions))

#                  precision  recall    f1-score                        support
#                   정밀도    재현율    정밀도와 재현율의 조화 평균
#            0       1.00      1.00      1.00                              9
#            1       0.92      0.92      0.92                             12
#            2       0.89      0.89      0.89                              9
print(classification_report(y_test,predictions))

#     accuracy                           0.93        30
#    macro avg       0.94      0.94      0.94        30
# weighted avg       0.93      0.93      0.93        30







