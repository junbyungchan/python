"""
우리가 만든 함수로 knn 적용해보기(iris)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scratch11.ex03 import train_test_split, MyScaler, MyKnnClassifier
from sklearn.metrics import  confusion_matrix, classification_report


if __name__ == '__main__':
    # 데이터 세트를 준비
    col_names = ['sepal_length','sepal_width','petal_length','petal_width','Class']
    iris = pd.read_csv('iris.csv', header = None, names = col_names)
    print(iris.iloc[:5])

    # 데이터 프레임을 이용해서 각 특성(변수)들과 Class(레이블)과의 관계 그래프
    # 산점도 그래프

    iris_by_class = iris.groupby(by='Class')
    for name,group in iris_by_class:
        # print(name,len(group))
        plt.scatter(group['sepal_length'],group['sepal_width'],
                    label = name)
    plt.legend()
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.show()

    for name,group in iris_by_class:
        # print(name,len(group))
        plt.scatter(group['petal_length'],group['petal_width'],
                    label = name)
    plt.legend()
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.show()

    # 데이터 세트를 points와 labels로 구분
    X = iris.iloc[: , : -1].to_numpy() # points /// Class 를 제외한 모든 행   // .to_numpy() 꼭 해주기
    y = iris.iloc[ : , 4].to_numpy() # labels  /// Class

    # 학습/검증(train/test) 세트로 분리
    X_train,X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2) # Ctrl + Alt  + 방향키 기능!

    # Scaling
    scaler = MyScaler() # 생성자 호출
    scaler.fit(X_train) # 스케일링 하기 위한 평균과 표준 편차 계산
    X_train = scaler.transform(X_train) # 데이터 변환 (스케일링 해주는 것)
    X_test = scaler.transform(X_test)

    # k-NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=9) # 분류기 객체 생성
    knn.fit(X_train,y_train) # 학습
    y_pred = knn.predict(X_test) # 예측
    print(np.mean(y_test == y_pred)) # 예측 결과 확인

    # Confusion Matrix 만들기
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))

    print('=============================================================================')


    # wisc_bc_data : 암 데이터
    wisc = pd.read_csv('wisc_bc_data.csv')
    print(wisc.iloc[:5,:])

    X_w = wisc.iloc[ : , 2: ].to_numpy()
    y_w = wisc.iloc[ : , 1].to_numpy()

    X_w_train, X_w_test, y_w_train , y_w_test = train_test_split(X_w,y_w, test_size= 0.2)

    scaler_w = MyScaler()
    scaler_w.fit(X_w_train)
    X_w_train = scaler_w.transform(X_w_train)
    X_w_test = scaler_w.transform(X_w_test)

    knn_w = MyKnnClassifier(n_neighbors=9)
    knn_w.fit(X_w_train,y_w_train)
    y_w_pred = knn_w.predict(X_w_test)
    print(np.mean(y_w_pred == y_w_test))

    print(confusion_matrix(y_w_test,y_w_pred))
    print(classification_report(y_w_test,y_w_pred))









