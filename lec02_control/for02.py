# 빈 리스트를 선언
# 난수(0<= x <= 100) 10개를 리스트에 저장
# 리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
# 리스트에 저장된 시험 점수 10개 중에서 최댓값, 최솟값으 찾아서 출력
import numpy as np
from math import sqrt


score = []
total = 0
for i in range(10):
    score.append(np.random.randint(0,101))
print(score)
for j in score:
    total += j
x = total
y = total/len(score)
print('총합: ',x)
print(f'총점2 = {sum(score)}') # sum() 총합을 구해주는 함수.
print('평균: ',y)
print(f'평균2 = {np.mean(score)}') # np.mean 넘파이 안에 평균을 내주는 함수가 존재한다.

# 표준편차 구하기 : from math import sqrt
z = 0
for k in score:
    z += (k-y) ** 2

v = z/len(score)
print('분산:',v)
std = sqrt(v)
print('표준편차:',std)
print(f'표준편차2 : {np.std(score)}')

# print(max(score))
# print(min(score))

max = score[0]
for i in range(1,len(score)):
    if max > score[i]: # max 보다 작으면 그냥 지나간다.
        pass
    else:
        max = score[i] # max 보다 크면 max 에 score[i]값을 할당한다.

print('최댓값: ',max)

min = score[0]
for i in range(1,len(score)):
    if min <= score[i]:
        pass
    else:
        min = score[i]

print('최솟값: ',min)

# 정렬해주는 함수 sorted(literable 변수,reverse=True) reverse ---> True 값 : 내림차순 
sorted_scores = sorted(score,reverse=True)
print(sorted_scores) # 새로운 리스트를 생성해준다.
print(score)