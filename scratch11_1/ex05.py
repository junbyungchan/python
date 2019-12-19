from collections import Counter

import numpy as np
import pandas as pd
import os
from scratch11_1.ex04 import separate_by_class, separate_by_class2, summarize_dataset, summarize_by_class, \
    calculate_class_probability
from sklearn.metrics import confusion_matrix, classification_report

def train_test_split(df, test_size):
    """ df : 데이터 프레임
        test_size : test set의 비율 (0.0 ~ 1.0)
        학습 세트(X_train)와 검증 세트(X_test)를 리턴
        train / test set: 리스트 이거나 nd.array
        [[ x1, x2, ..., label1] , [ x1, x2, ..., label2] , [], ...] , [[] , [] , [], ...]
        """

    # DataFrame을 numpy.ndarray 타입으로 변환
    array = df.to_numpy()
    # array의 순서를 무작위로 섞는다.
    np.random.seed(1213)
    np.random.shuffle(array)
    # 학습 세트/ 테스트 세트를 나누기 위한 인덱스
    cut = int(len(array) * (1-test_size)) # array의 인덱스는 정수가 되야하므로 int()로 묶어줌.
    # 학습 세트와 테스트 세트로 나누기
    train_set = array[ : cut]
    test_set = array[cut : ]
    # 결과 리턴
    return train_set, test_set

def predict(summaries, X_test):
    """ 테스트 세트의 예측값들의 배열(리스트)을 리턴
        [0,1,1,2,0,0,2 ..."""
    # X_test의 원소 개수만큼 반복하면서
    predicts = [] # 빈 리스트 생성
    for test in X_test:
        # 각 원소(테스트하려는 데이터)의 클래스에 속할 확률을 계산
        probabilities = calculate_class_probability(summaries,test)
        # 각 클래스에 속할 확률들 중에서 최댓값을 찾음

        # 다른 방법
        best_label , _ = sorted(probabilities.items(), key=lambda x: -x[1])[0] # lambda의 리턴 값 => (class 값 , 확률 값) 확률 값에 음수를 주므로써 내림차순으로 바뀐다.
        # sorted(Iterable, key= 정렬기준함수)  ----> 정렬기준 함수의 리턴값을 기준으로 Iterable객체를 정렬하겠다. 라는 의미
        # 정렬 기준 함수의 리턴값을 기준으로 Iterable 타입을 정렬한다.
        # sorted(dict): dict의 키들을 오름차순 정렬한 리스트
        # sorted.(dict.values()) : dict의 값들을 오름차순 정렬한 리스트
        # sorted.(dict.items()) : (key,value) 튜플을 key값을 기준으로 정렬

        # best_label , best_prob = None , -1
        # for k , v in probabilities.items():
        #     if v > best_prob : # 더 큰 확률값을 찾은 경우
        #         best_prob = v # 찾은 확률값으로 best_prob을 업데이트
        #         best_label = k # 찾은 확률값의 키를 best_label을 업데이트
        # 확률 최대값의 키값을 예측값 리스트에 추가
        predicts.append(best_label)
    return predicts

if __name__ == '__main__':
    iris_file = os.path.join('..','scratch11','iris.csv')

    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris_dataset = pd.read_csv(iris_file,header= None , names=col_names) # iris 데이터는 header가 없으므로
    print(iris_dataset.shape) # (150,5)  = (행의 개수, 컬럼의 개수 )
    print(iris_dataset.iloc[ : , -1]) # DataFrame의 가장 마지막 컬럼

    # iris 품종 : Iris-setosa, Iris-versicolor, Iris-virginica
    # iris 품종을 보려면 set()으로 적용하면 중복된 값이 지워져서 종류만 알아낼 수 있다.
    species = set(iris_dataset.iloc[:,-1])
    print(species) # 출력 {'Iris-setosa', 'Iris-virginica', 'Iris-versicolor'}

    # iris_class 의 3 종류를 숫자형태로 0,1,2
    # 'Iris-setosa' = 0 , 'Iris-versicolor' = 1 , 'Iris-virginica' = 2 로 변경
    # boolean 형 인덱스
    iris_dataset.loc[iris_dataset['Class'] == 'Iris-setosa' , 'Class'] = 0
    iris_dataset.loc[iris_dataset['Class'] == 'Iris-versicolor', 'Class'] = 1
    iris_dataset.loc[iris_dataset['Class'] == 'Iris-virginica', 'Class'] = 2

    # set 형도 for _ in 구문으로 할 수 있으므로 위의 코드를 for 문으로 돌릴 수 있는 것을 생각해보자
    # for i in species:
    #     iris_dataset.loc[iris_dataset['Class'] == i,'Class'] = 0

    species = set(iris_dataset.iloc[:, -1])
    print(species) # {0, 1, 2}
    species_counts = Counter(iris_dataset.iloc[:,-1])
    print(species_counts) # Counter({0: 50, 1: 50, 2: 50})

    # 출력
    iris_train , iris_test = train_test_split(iris_dataset,test_size=0.2)
    print('Train set:', iris_train.shape)
    print('Test set:', iris_test.shape) # [:5] - 처음 5개 원소, [-5:] - 마지막 5개 원소

    # 학습 데이터 세트만으로 summaries( 평균, 표준 편차, 개수) 를 찾는다.
    model = summarize_by_class(iris_train) # GaussianNB에서 사용할 mu, sigma
    print(model)
    print(model[0.0])

    # 검증(테스트) 데이터 세트로 모델에서 예측하는 값들을 찾음.
    iris_pred = predict(model,iris_test)
    print(iris_pred)
    # iris_test 와 iris_pred 를 비교하면 얼마나 정확도를 맞췄는지 알수 있다.
    print(iris_test[:, -1] == iris_pred)

    # 정확도를 보는 confusion_matrix, classification_report
    print(confusion_matrix(iris_test[:,-1],iris_pred))
    print(classification_report(iris_test[:,-1],iris_pred))

    # 암 데이터
    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')
    # 데이터 준비
    cancer_dataset = pd.read_csv(cancer_file)

    # 데이터 확인
    print(cancer_dataset.head())
    # 컬럼의 데이터 타입 확인
    cancer_dataset.info()

    # 데이터 전처리 - 'id' 삭제, 'diagnosis' 변수(컬럼) 값들을 숫자로 변환
    # cancer_dataset.drop(columns='id')
    # inplace= False ---> 원본 데이터 프레임은 남겨두고 새로운 데이터 프레임을 리턴해주겠다.
    # 행을 지울때 axis= 0
    # 원본 데이터 프레임은 그대로 남아 있고, 컬럼이 삭제된 새로운 데이터 프레임을 리턴
    del cancer_dataset['id']  # ---> 원본 데이터 프레임에서 컬럼을 삭제

    diagnosis = set(cancer_dataset['diagnosis']) # diagnosis 컬럼만 추출해서 diagnosis에 넣겠다.
    print(diagnosis)
    # B(Benign)양성 = 0 (종양이 아닌 경우) , M(Malignant)악성 = 1 (종양인 경우)

    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'B' , 'diagnosis'] = 0
    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'M' , 'diagnosis'] = 1
    # del cancer_dataset['diagnosis']
    # print(cancer_dataset.tail())

    # diagnosis 컬럼을 데이터 프레임의 마지막 컬럼으로
    column_names = cancer_dataset.columns.tolist() # 원본의 데이터 프레임에서 컬럼의 이름들을 리스트로 추출
    print(column_names)
    #
    column_names.remove('diagnosis')
    column_names.append('diagnosis')
    print(column_names)
    df = cancer_dataset.reindex(columns= column_names)
    print(df)
    # 다른 방법
    df1 = cancer_dataset[column_names]
    print(df1)
    # 또 다른 방법
    df2 = cancer_dataset.loc[:,::-1]
    print(df2) # 컬럼을 좌우 반전 시킨다.


    cancer_train , cancer_test = train_test_split(df, test_size=0.2)
    cancer_model = summarize_by_class(cancer_train)
    cancer_predict = predict(cancer_model,cancer_test)
    print(confusion_matrix(cancer_test[:,-1], cancer_predict))
    print(classification_report(cancer_test[:,-1],cancer_predict))











