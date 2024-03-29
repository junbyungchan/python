"""
List comprehension
# 리스트 이름 변수 = [리스트에 각각 저장될 변수를 포함한식/ for /변수 /in /범위]
"""
import numpy as np

numbers = [1,2,3,4,5]
print(numbers)

numbers2 = []
for i in range(1,6):
    numbers2.append(i)
print(numbers2)

numbers3 = [n for n in range(1,6)] # list comprehension  한줄로 표현
print(numbers3)

# 2,4,6,8,10 를 리스트에 저장
even = [2*n for n in range(1,6)] # 리스트 이름 변수 = [리스트에 각각 저장될 변수를 포함한식/ for /변수 /in /범위]
print(even)

# 1,4,9,16,25
squares = [n**2 for n in range(1,6)]
print(squares)

# 난수 10개 배열
randoms = [np.random.randint(1,101) for _ in range(1,11)] # 리스트에 저장할 숫자는 np.random.randint(1,101) 난수 인데 for문의 변수는 필요없는 변수이므로
# 형식만 맞춰주기 위해서 _로 표현가능하다.
print(randoms)

even2 = []
for n in range(1,11):
    if n % 2 == 0:
        even2.append(n)
print(even2)

even3 = [n for n in range(1,11) if n % 2 == 0] # ---> if문도 더해줄수 있다.
print(even3)

# 주사위 2개를 던졌을때 경우의 수
# (1,1),(1,2),(1,3),(1,4),(1,5),(1,6)
# (2,1),(2,2) ....
# ...
# (6,1), .... (6,6)
dice1 = []
for x in range(1,7):
    for y in range(1,7):
        dice1.append((x,y)) # (x,y) tuple을 리스트에 추가

print(dice1)

# 두 개의 반복문을 list comprehension으로 가능하다.
dice2 = [(x,y) for x in range(1,7) for y in range(1,7)]
print(dice2)

# (1,1)
# (2,1), (2,2)
# (3,1), (3,2), (3,3)
# (x,y) if x>=y
dice3 = []
for x in range(1,7):
    for y in range(1,7):
        if x >=y:
            dice3.append((x,y))
print(dice3)

dice4 = [(x,y)
         for x in range(1,7)
         for y in range(1,7)
         if x >= y] # 줄 바꿔서 실행해도 가능하다
print(dice4)

# 학생들의 점수(0~100) 10개짜리 리스트
scores = [np.random.randint(0,101) for _ in range(10)]
print(scores)
# 평균보다 높은 점수들의 리스트
mean = np.mean(scores)
above_mean = [s for s in scores if s > mean]
# above_mean = []
# for s in scores:
#     if s > mean:
#         above_mean.append(s)
print(above_mean)








