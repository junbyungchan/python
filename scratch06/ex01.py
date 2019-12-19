"""
scratch06\ex01.py
확률

사건 공간(universe of events)
사건(event)
확률(probability)
"""
import random
from collections import Counter


coin = ['H','T']
dice = [1,2,3,4,5,6]
trials = 10_000 # 쉼표대신 언더바를 사용해서 숫자의 자릿수를 알수 있다.
print(random.choice(dice))

# 동전 1개를 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2 임을 증명
k = []
for _ in range(0,10000): # 10,000번 반복
    k += random.choice(coin)
print(Counter(k))
# 강사님 답안
heads, tails = 0,0 # 앞면과 됫문여 나오는 횟수를 저장할 변수
for _ in range(trials): # 10,000번 반복
    random_coin = random.choice(coin) # 동전 던진 결과(앞 또는 뒤)
    if random_coin == 'H':
        heads += 1
    else:
        tails += 1
p_h = heads / trials
p_t = tails / trials
print('P(H) =',p_h)
print('P(T) =',p_t)

# 동전 2개를 던지는 실험(10,000번)
# 1) 앞면의 개수가 1개일 확률 1/2 (HT, TH)
# 2) 첫번째 동전이 앞면일 확률 1/2 (HH, HT)
# 3) 적어도 한개의 동전이 앞면일 확률 3/4 (HH, HT, TH)
# = 1 - 두개 동전 모두 뒷면일 확률

# 1)
h_c , t_c = 0,0
for _ in range(trials):
    random_coin = random.choice(coin)
    random_coin1 = random.choice(coin)
    if (random_coin == 'H' and random_coin1 == 'T') or (random_coin == 'T' and random_coin1 == 'H'):
        h_c += 1
    else:
        t_c += 1
p_h = h_c / trials
p_t = t_c / trials
print('앞면의 개수가 1개일 확률 =',p_h)
print('그 이외일 확률 =',p_t)

# 2)
f_h , f_t = 0,0
for _ in range(trials):
    random_coin = random.choice(coin)
    random_coin1 = random.choice(coin)
    if (random_coin =='H'):
        f_h += 1
    else:
        f_t += 1
f_h = f_h / trials
f_t = f_t / trials
print('첫번째 동전이 앞면일 확률 =', f_h)
print('첫번째 동전이 앞면이 아닐 확률 =',f_t)

# 3)
o_h , o_t = 0,0
for _ in range(trials):
    random_coin = random.choice(coin)
    random_coin1 = random.choice(coin)
    if (random_coin == 'H') or (random_coin1 == 'H') or ( random_coin == 'H' and random_coin1 == 'H'):
        o_h +=1
    else:
        o_t +=1
f_o_h = o_h / trials
f_o_t = o_t / trials
print(f_o_h)
print(f_o_t)

# 동전 3개를 던지는 실험(10,000번)
# 앞면의 개수가 1개일 확률 3/8 (HTT, THT, TTH)
count = 0
for _ in range(trials):
    random_coin = random.choice(coin)
    random_coin1 = random.choice(coin)
    random_coin2 = random.choice(coin)
    if random_coin =='H'  and random_coin1 == 'T' and random_coin2 == 'T':
        count += 1
    elif random_coin =='T'  and random_coin1 == 'H' and random_coin2 == 'T':
        count += 1
    elif random_coin == 'T' and random_coin1 == 'T' and random_coin2 == 'H':
        count += 1

print(count, count / trials)

# 강사님 답안

def experiment(type,n,t): #======================================================experiment
    """
    :param type: 실험 타입(동전 던지기 or 주사위 던지기, ...)
    :param n: 동전의 개수
    :param t: 실험 횟수
    :return: 리스트트
   """
    cases = [] # 동전 던지기 실험 결과를 저장
    for _ in range(t): # 실험 횟수만큼 반복
        case = [] # 각 실험의 결과를 저장
        for _ in range(n): # 동전 개수만큼 반복
            random_coin = random.choice(type) # 'H' or 'T'
            case.append(random_coin) # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 tuple로 변환 후 저장
        # Counter 클래스는 tuple의 개수는 셀 수 있지만,
        # list의 개수는 셀 수 없음!
        cases.append(tuple(case))
    return cases


coin_exp = experiment(coin, 2, 10_000)
print(coin_exp[0:10]) # 첫 10개의 실험 결과 확인

# 동전 던지기 실험 경우의 수
coin_event_counts = Counter(coin_exp) # 리스트는 정렬을 할수가 없기 때문에
# 튜플로 전환해서 계산하자
print(coin_event_counts)

def how_many_heads(x):
    counter = Counter(x)
    print(counter)
    return counter['H']

num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_heads(ev) ==1:
        num_of_cases += cnt
        p_h1 = num_of_cases / trials
print('앞면이 1개일 확률 =' , p_h1)

num_of_cases = 0
for ev ,cnt in coin_event_counts.items():
    # if ev == ('H','H') or ev == ('H','T'):
    if ev[0] == 'H':
        num_of_cases += cnt
p_first_h = num_of_cases / trials
print('P(첫번째 동전이 앞면) =',p_first_h)

num_of_cases = 0
for ev ,cnt in coin_event_counts.items():
    if how_many_heads(ev) == 1 or how_many_heads(ev) == 2: # 앞면이 하나 또는 두개 나올 확률
        num_of_cases += cnt
p = num_of_cases / trials
print('P(적어도 1개가 앞면) =', p)

# 여사건 이용
num_of_cases = 0
for ev , cnt in coin_event_counts.items():
    if how_many_heads(ev) == 0: # 앞면이 모두 안나올 확률
        num_of_cases += cnt
p = num_of_cases / trials
print('P(적어도 1개가 앞면) =', 1-p)

# H = 1, T = 0 약속 -> coin = [1,0]
coin2 = [1,0]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2):
        if 1 == random.choice(coin2):
            num_of_heads += 1
    cases.append(num_of_heads)
print(cases[0:10])
coin_event_counts = Counter(cases)
print('P(H=0) =', coin_event_counts[0] / trials)
print('P(H=1) =', coin_event_counts[1] / trials)
print('P(H=2) =', coin_event_counts[2] / trials)

# 1) : 주사위 2개를 던졌을 때, 두 눈의 합이 8 일 확률
# (2,6) , (3,5), (4,4) , (5,3) , (6,2) ===> 5/36
# 2) : 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률
# (1,1) (1,3), (1,5), (3,1), (3,3) , (3,5) ,
# (5,1), (5,3) , (5,5)를 제외한 모든 경우 => 27/36

# 내 답
# 1)
dice_exp = experiment(dice,2,10_000)
dice_event_counts = Counter(dice_exp)
print(dice_event_counts)
print(dice_event_counts.items())
num_count = 0
for a,b in dice_event_counts.items():
    if a[0] + a[1] == 8:
        num_count += b
print(num_count / trials)

# 2)
num_count = 0
for a,b in dice_event_counts.items():
    if a[0] % 2 == 1 and a[1] % 2 == 1:
        num_count += b
print(1 - (num_count/trials))

# 강사님 답안
# 1)
event_counts = Counter(dice_exp)
print(len(event_counts))
print(event_counts)
num_of_cases = 0
for ev, cnt in event_counts.items():
    # if ev[0] + ev[1] == 8:
    if sum(ev) == 8:
        num_of_cases += cnt
p = num_of_cases / trials
print('P(두 눈의 합=8) =', p, 5/36)
# 2)
num_of_cases = 0
for ev, cnt in event_counts.items():
    if ev[0] % 2 == 0 or ev[1] % 2 == 0:
        num_of_cases += cnt
p = num_of_cases / trials
print('P(적어도 하나가 짝수) =', p , 27/36)



