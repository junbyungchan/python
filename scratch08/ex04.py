"""
선형 회귀(Linear Regression)
모델 : y = ax + b에서, 기울기(slope) a 와 y 절편 b를 찾는 문제

(a, b)를 임의의 값으로 가정했을 때의 예상값과 실제값 사이의 오차들의
제곱의 합을 최소로 하는 a와 b를 찾는 문제이다.
실제값 (x, y)
예상값: y_hat = theta1 * x + theta2
오차(에러) : e = y_hat - y = theta1 * x + theta2 -y
오차 제곱: f = e ** 2 = (theta1 * x + theta2 -y) ** 2
기울기 theta1에 대한 편미분 : df/dt1 ~ e * x
y절편 theta2에 대한 편미분: df/dt2 ~ e

---> '~' 의 의미는 비슷해진다의 의미 ,
---> dt1, dt2 는 라운드 theta1 , 라운드 theta2 를 의미한다.

1) 확률적 경사 하강법(Stochastic Gradient Descent)
    전체 데이터 세트(훈련 세트)에서 샘플 데이터 1개씩 gradient를 계산.
    각 데이터마다 파라미터(기울기, 절편)를 변경.
    위 과정을 임의의 회수(epoch)만큼 반복한다.
===> (x, y)을 이용해서 각 gradient를 구해서 세타값을 변경한다. 세타가 gradient수 만큼 변경된다.

2) 배치 경사 하강법(Batch GD)
    전체 데이터 세트를 사용해서 전체 gradient들의 평균을 gradient로 사용해서
    파라미터 theta를 변경
    위 과정을 임의의 회수(epoch)만큼 반복한다.
===> (x, y)을 이용해서 각 gradient를 구해서 gradient의 평균을 구해서 gradient의 평균으로 세타값을 한번만 변경한다.
===> 단점 : epoch의 수를 크게 해야한다.

3) 미니 배치 경사 하강법(Mini-batch GD)
    전체 데이터 세트를 크기를 작게 샘플링해서 처리하는 방식.
    각각의 epoch(반복)마다 데이터 세트의 순서를 섞어서 파라미터(theta)의 최적값을 찾는다.
===> 위의 2개의 절충안으로 나온 방법
===> (x, y)을 이용해서 각 gradient를 구한다.
===> 적절한 갯수로 gradient를 짤라서 그 갯수만큼의 평균을 이용해서 세타를 변경한다.
===> 변경된 세타를 이용해서 다음 똑같은 갯수의 (x,y)의 gradient를 구해서 평균을 내서 세타값을 변경한다.
===> 이런 방식을 계속 사용한다.

GD ==> Gradient Descent
"""

# 메소드 정의
import random

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step


def linear_gradient(x, y , theta):
    """특정 데이터 (x, y)에서 기울기와 y절편에 대한 편미분 벡터를 리턴하는 함수

    :param x: 실제 데이터
    :param y: 실제 데이터
    :param theta: [theta1 , theta2] 벡터(리스트). [기울기, y절편]
    """
    slope, intersect = theta
    y_hat = slope * x + intersect  # 예상값 = y_hat = a * x + b
    error = y_hat - y # 오차
    # error ** 2 값을 최소화 하는 slope(기울기), intersect(y 절편) 을 찾자.
    # 점(x, y)에서  [기울기에 대한 편미분, 절편에 대한 편미분]
    gradient = [error * x, error]

    return gradient
    # 미분 --> 변화량

def minibatches(dataset, batch_size, shuffle=True):
    # 데이터 세트를 무작위로 섞음
    if shuffle:
        random.shuffle(dataset)
    # 배치 시작 인덱스: 0, batch_size, 2*batch_size, ...
    batch_starts = [s for s in range(0,len(dataset), batch_size)]
    mini = [dataset[s:s+batch_size] for s in batch_starts]

    return mini


dataset = [(x, 20 * x + 5) for x in range(-50,50)]

if __name__ == '__main__':
    print('===확률적 경사 하강법===')
    # 임의의 파라미터 초깃값
    random.seed(1129)
    theta = [1 , 1 ] # [기울기, 절편], y = x + 1
    # 파라미터의 값을 변경할 때 사용할 가중치
    step = 0.001 # next_x = init_x + step * gradient 에서의 step이다.

    for epoch in range(200): # 임의의 횟수(epoch)만큼 반복
        random.shuffle(dataset) # 데이터 세트를 랜덤하게 섞음
        # 각각의 epoch마다
        # 데이터 세트에서 샘플(x,y)를 추출
        for x,y in dataset:
            # 각 점에서 gradient를 계싼
            gradient = linear_gradient(x, y ,theta)
            # 파라미터 theta(직선의 기울기와 절편)를 변경
            theta = gradient_step(theta,gradient, - step)
        if (epoch + 1) % 10 == 0:
            print(f'{epoch}: {theta}')

    print('\n===배치 경사 하강법 ===')
    step = 0.001
    theta = [1,1] # 임의의 값으로 [기울기, 절편] 설정
    for epoch in range(5000):
        # 모든 샘플에서의 gradient를 계산
        gradients = [linear_gradient(x,y,theta)
                     for x,y in dataset]
        # gradients의 평균을 계산해야한다.
        gradient = vector_mean(gradients)
        # 파라미터 theta(기울기, 절편)을 변경
        theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')

    print('\n=== 미니 배치 하강법 ===')
    theta = [1,1] # 임의의 파라미터 시작값
    step = 0.001 # 학습률
    for epoch in range(1000):
        mini_batches = minibatches(dataset,20,True)
        for batch in mini_batches:
            gradients = [linear_gradient(x,y,theta)
                         for x,y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta,gradient,-step)
            if (epoch + 1 ) % 100 == 0 :
                print(f'{epoch} : {theta}')













