"""
사건의 종속성 vs 독립성
사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속 사건(dependent event).
사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 사건 B는 독립 사건(independent event).

동전 2개를 던지는 경우,
A: 첫번째 동전이 앞면
B: 두번째 동전이 뒷면
C: 두 동전 모두 뒷면(앞면)
A와 B는 독립 사건.
A와 C는 종속 사건.

P(A):사건 A가 일어날 확률
P(B):사건 B가 일어날 확률
p(A,B):사건 A와 사건 B의 교집합이 일어날 확률(동시에 일어날 확률)

P(A,B) = P(A) * P(B) 이 성립하면, 두 사건은 독립 사건.
"""
import random
# 자녀가 2명인 경우,
# A: 첫째가 딸인 경우
# B: 둘째가 아들인 경우
# C: 둘 다 딸인 경우
# A와 B가 독립 사건, A와 C는 종속 사건임을 증명
# P(A), P(B), P(C), P(A,B) , P(A,C)

child = ('boy','girl')
trials = 10000

event_a=0
event_b=0
event_c=0
event_a_b = 0
event_a_c = 0
for _ in range(trials):
    first = random.choice(child)
    second = random.choice(child)
    if first == 'girl':
        event_a += 1
    if second == 'boy':
        event_b += 1
    if first == 'girl' and second == 'boy':
        # 사건 A와 사건B의 교집합
        event_a_b += 1
    if first == 'girl' and second == 'girl':
        event_c += 1
    if first =='girl' and (first == 'girl' and second == 'girl'):
        # 사건 A와 사건 C의 교집합
        event_a_c += 1

p_a = event_a / trials
p_b = event_b / trials
p_a_b = event_a_b / trials
p_c = event_c / trials
p_a_c = event_a_c / trials



