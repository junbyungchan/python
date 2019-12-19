"""
scikit-learn 패키지에 포함된 위스콘신 대학 암 데이터를 로딩해서
Naive Bayes 모델로 예측 결과를 분석
"""
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_breast_cancer(return_X_y=True)

X_train ,X_test , y_train, y_test = train_test_split(X, y , test_size= 0.2)

scaler = StandardScaler()
scaler.fit(X_train, y_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

# 머신러닝 모델 선택
gnb = GaussianNB()
gnb.fit(X_train_transformed, y_train)
y_pred = gnb.predict(X_test_transformed)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

