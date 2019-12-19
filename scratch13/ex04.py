import numpy as np

# numpy.c_ 와 numpy.r_의 비교
a = np.array([1,2,3])
print(a, type(a), a.shape)
b = np.array([4,5,6])
print(b, type(b), b.shape)

c = np.c_[a,b]
print(c, type(c), c.shape)   # 첫번째 칼럼이 새로운 배열의 첫 행이 된다.
# [[1 4]
#  [2 5]
#  [3 6]] <class 'numpy.ndarray'> (3, 2)

d = np.r_[a,b]
print(d, type(d), d.shape)
# [1 2 3 4 5 6] <class 'numpy.ndarray'> (6,)

# 2차원 이상일 때 어떻게 동작하는지 해보자
e = np.array([[1,2,3],
              [4,5,6]])

f = np.array([[7,8],
              [9,10]])

print(np.c_[e,f]) # e 와 f 의 row 개수가 같아야 column 방향으로 붙일 수 있다.
# print(np.r_[e,f]) # e 와 f 의 column 개수가 다르면 row 방향으로 붙일 수 없다!

g = np.array([[100,200,300]])
# print(np.c_[e,g]) # row의 개수가 다르기 때문에 column 방향( 오른쪽) 으로 붙일 수 없음!
print(np.r_[e,g]) # column의 개수가 같아야 밑으로 붙일 수 있음.

# (2,3) shape의 모든 원소가 1인 array를 생성해서 출력 : a
a = np.ones((2,3), dtype=int)
print(a)
# (2,3) shape의 모든 원소가 0인 array를 생성해서 출력 : b
b = np.zeros((2,3), dtype=int)
print(b)
# (3,2) shape의 원소가 1 ~ 6 인 array를 생성해서 출력 : c
c = np.arange(1,7).reshape((3,2))
print(c)
# (3,2) shape의 난수들로 이루어진 array를 생성해서 출력  : d
d = np.random.random((3,2))
print(d)

"""다음과 같은 결과가 나올 수 있도록 
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
|1 2| + |5 6|= |6  8 | 
|3 4|   |7 8|  |10 12|

|1 2| - |5 6|= |-4 -4| 
|3 4|   |7 8|  |-4 -4|

|1 2| * |5 6|= |5  12| 
|3 4|   |7 8|  |21 32|

|1 2| / |5 6|= |0.2   0.333| 
|3 4|   |7 8|  |0.428 0.5  |

|1 2| @ |5 6|= |19 22| 
|3 4|   |7 8|  |43 50|
위의 결과와 같은 결과를 주는 numpy 코드를 작성
"""
x = np.array([[1,2],
            [3,4]])
y = np.array([[5,6],
            [7,8]])
def add(x,y):
    list = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            list.append(x[i][j] + y[i][j])
    a = np.array(list)
    a = a.reshape(len(x),len(x[0]))
    return a
print(add(x,y))

def subtract(x,y):
    list = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            list.append(x[i][j] - y[i][j])
    b = np.array(list)
    b = b.reshape(len(x), len(x[0]))
    return b
print(subtract(x,y))

def multiply(x,y):
    list = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            list.append(x[i][j] * y[i][j])
    c = np.array(list)
    c = c.reshape(len(x), len(x[0]))
    return c
print(multiply(x,y))

def divide(x,y):
    list = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            list.append(round(x[i][j] / y[i][j],3))
    d = np.array(list)
    d = d.reshape(len(x), len(x[0]))
    return d
print(divide(x,y))


def my_dot(x,y):
    list=[]
    for i in range(len(x)):
        temp = []
        for j in range(len(y[0])):
            val = 0
            for k in range(len(x[0])):
                val += x[i][k] * y[k][j]
            temp.append(val)
        list.append(temp)
    e = np.array(list)
    e = e.reshape(len(x), len(x[0]))
    return e
print(my_dot(x,y))

def tea_dot(A,B):
    """
    두 행렬 A와 B의 dot 연산 결과를 리턴
    dot_ik = sum(j)[a_ij * b_jk]
    """
    print('A shape' , A.shape)
    print('B shape' , B.shape)
    if A.shpae[1] != B.shape[0]:
        raise ValueError('A의 column과 B의 row 개수가 같아야함!')
    numbers = []
    n_row = A.shape[0] # dot 결과 행렬의 row 개수
    n_col = B.shape[1] # dot 결과 행렬의 column 개수
    temp = A.shape[1] # 각 원소들끼리 곱한 결과를 더하는 횟수
    for i in range(n_row): # A행렬의 row 개수만큼 반복
        for k in range(n_col): # B 행렬의 column 개수만큼 반복
            n = 0
            for j in range(temp):
                # dot 결과 행렬의 [i,k] 번째 원소의 값을 계산
                n += A[i,j] * B[j,k]
            numbers.append(n) # [i,j] 번째 원소를 리스트에 추가
    # 결과를 (n_row,n_col) 모양의 행렬로 변환해서 리턴
    return np.array(numbers).reshape(n_row,n_col)
print(my_dot(x,y))
print(x.dot(y))
print(my_dot(y,x))
print(y.dot(x))
print('=====================')






"""
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬
"""
# 항등행렬
I = np.eye(3)
print(I)

# 역행렬
x_inv = np.linalg.inv(x)
print(x_inv)

# 전치행렬
print(x.T)




