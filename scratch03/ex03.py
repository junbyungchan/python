"""
산점도 그래프(Scatter plot)
 - 점으로 표시하는 그래프
"""

import matplotlib.pyplot as plt

# 친구 수
# 갯수를 맞춰야 한다.
friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)
for l,f,m in zip(labels,friends,minutes):
    plt.annotate(l,
             xy=(f,m),
             xytext=(5,-5), # xytext == a를 어디에다가 표현할것이냐 xy의 기준점으로 70 +5 , 175 -5
             textcoords = 'offset points') #

plt.title('Minutes vs Friends') # 제목
plt.xlabel('# of friends') # x 축 아래에 레이블 생성
plt.ylabel('average time(minutes)') # y축 옆에 레이블 생성

plt.show()

math = [99,90,85,97,80]
science = [100,85,60,90,70]

plt.scatter(math,science)
plt.axis('equal')

plt.title('Science vs Math')
plt.xlabel('Math')
plt.ylabel('Science')
plt.show()
