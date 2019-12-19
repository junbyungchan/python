"""
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장 x
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사 x
3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
4) 선형 회귀식	cty = slope * displ + intersect의 기울기(slope)와 절편(intersect)을
경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
"""
import csv
import random
import matplotlib.pyplot as plt

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step
from scratch08.ex04 import linear_gradient, minibatches

data = []

f = open('mpg.csv','r')
mpg = csv.reader(f)

for line in mpg:
    data.append(line)
data = data[1: ]
f.close()

m = []
for x in data:
    m.append([x[3],x[8]])

print(m)
for x in range(len(m)):
    for i in range(0,2):
        m[x][i] = float(m[x][i])
print(m)


# displ = displ[1: ]  # 첫번째 displ 삭제
# cty = cty[1: ]     #  첫번째 cty 삭제
#
# print(displ) # 리스트 형식으로 뽑았다     x의 값이 되고
# print(cty) # 리스트 형식으로 뽑았다.      y의 값이 되는거다.

if __name__ == '__main__':
    print('===확률적 경사 하강법===')
    theta = [1,1]
    step = 0.001
    random.seed(1129)

    for epoch in range(200):
        random.shuffle(m)
        for x,y in m:
            gradient = linear_gradient(x,y,theta)
            theta = gradient_step(theta,gradient,-step)
        if (epoch + 1) % 10 == 0:
            print(f'{epoch}: {theta}')


    print('\n===배치 경사 하강법 ===')
    step = 0.1
    theta = [1, 1]
    for epoch in range(500):
        gradients = [linear_gradient(x, y, theta)
                     for x, y in m]
        gradient = vector_mean(gradients)
        theta = gradient_step(theta,gradient,-step)
        if (epoch + 1) % 10 == 0:
            print(f'{epoch}: {theta}')


    print('\n=== 미니 배치 하강법 ===')
    step = 0.1
    theta = [1, 1]
    for epoch in range(1000):
        mini_batches = minibatches(m, 20, True)
        for batch in mini_batches:
            gradients = [linear_gradient(x, y, theta)
                         for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -step)
            if (epoch + 1 ) % 100 == 0 :
                print(f'{epoch} : {theta}')

# step을 바꾸어 가면서 찾아봐야한다. step --> 학습률
# -2.6 , 25.6 언저리

x = []
y = []
for i in m:
    x.append(i[0])
    y.append(i[1])

print(x)
print(y)