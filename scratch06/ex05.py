"""
확률 변수 (Random variable):
    어떤 확률 분포와 연관되어 있는 변수
    (예) 동전 1개를 던지는 확률 분포에서, 동전 앞면의 개수 X
    P(X=1) = 1/2, P(X=0) = 1/2
    (예) 주사위 1개를 던지는 확률 분포에서, 주사위 눈의 개수 X
    X = 1, 2, 3, 4, 5, 6
기댓값(expected value):
    확률 변수의 확률에 확률 변수의 값을 가중 평균한 값
    E(X) = sum(x_i * P(X=x_i))
    (예) 동전 1개를 던질 때, 동전 앞면의 기댓값
    E = 1 * 1/2 + 0 * 1/2 = 1/2 = 0.5
    (예) 주사위 1개를 던질 때, 주사위 눈의 기댓값
    E = 1 * 1/6 + 2 * 1/6 + ... + 6 * 1/6 =

"""

# 동전 3개를 던질 때, 확률 변수를 동전의 앞면의 개수
# X = 0, 1, 2, 3
# 동전 3개를 10,000번 던지는 실험
# -> P(X=0) = 1/8 , P(X=1) = 3/8 , P(X=2) = 3/8 , P(X=3) = 1/8
# -> 기대값 계산 ( 0*1 + 1*3 + 2*3 + 3*1 ) / 8 = 1.5
import random

# coin = ('H','T')
# coin1 = random.choice(coin)
# coin2 = random.choice(coin)
# coin3 = random.choice(coin)
# no_h = 0
# one_h = 0
# two_h = 0
# all_h = 0
# trials = 10_000
#
# for _ in range(trials):
#     if coin1 == 'H' or coin2 == 'H' or coin3 == 'H':
#         one_h += 1
#     if (coin1 == 'H' and coin2 =='H') or (coin1 == 'H' and coin3 =='H') or (coin2 == 'H' and coin3 =='H'):
#         two_h += 1
#     if (coin1 == 'H' and coin2 =='H' and coin3 == 'H'):
#         all_h += 1
#
# p_one_h = one_h / trials
# p_two_h = two_h / trials
# p_all_h = all_h / trials
# p_no_h = 1 - p_all_h
#
# print(p_one_h,p_two_h,p_all_h,p_no_h)

# 강사님 답
from collections import Counter

experiments = [] # 동전 3개를 10,000 던질때 , 동전 앞면의 개수
coin = (1,0) # 1=앞면 , 0 = 뒷면
trials = 10_000
for _ in range(trials):
    heads = 0 # 동전 앞면의 개수
    for _ in range(3):
        heads += random.choice(coin)
    experiments.append(heads)
print(experiments[0:10])

head_counts = Counter(experiments)
print(head_counts)

expected_value = 0 # 기댓값
for x, cnt in head_counts.items(): # Counter({2: 3781, 1: 3676, 3: 1288, 0: 1255})
    # key ===> x 는 2 , 1, 3, 0  value ===> cnt  해당 하는 갯수
    expected_value += x * cnt/trials
print('기댓값 =' ,expected_value)



# 주사위 눈의 기댓값
dice = (1,2,3,4,5,6)

experiments = [random.choice(dice) for _ in range(trials)]
print(experiments[0:10])
head_counts = Counter(experiments)
print(head_counts)
expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * cnt/trials
print('기댓값 =',expected_value)


