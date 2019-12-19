import matplotlib.pyplot as plt
import pandas as pd

col_names = ['sepal-length','sepal-width','petal-length','petal-width','Class']

iris = pd.read_csv('iris.csv',header=None, names= col_names)
iris_by_class = iris.groupby(by = 'Class')
print('=')
print(iris_by_class)

xy=[] # x축/y축에 사용할 변수 이름
for i in range(4):
    for j in range(i+1,4):
        xy.append((col_names[i],col_names[j]))

print(xy)

fig , ax = plt.subplots(2,3) # plt.subplots(2,3) ==> 하나의 figure의 모양을 2 X 3으로 나누겠다.
xy_idx = 0
for row in range(2):
    for col in range(3):
        axis = ax[row,col] # axis = ax[row][col]
        x = xy[xy_idx][0] # x 축 데이터 이름
        y = xy[xy_idx][1] # y 축 데이터 이름
        xy_idx += 1
        axis.set_title(f'{x} vs {y}') # plot 축의 제목
        axis.set_xlabel(x) # subplot 축의 x 레이블
        axis.set_ylabel(y) # subplot 축의 y 레이블
        for name, group in iris_by_class:
            axis.scatter(group[x],group[y], label = name)

plt.legend()
plt.show()
