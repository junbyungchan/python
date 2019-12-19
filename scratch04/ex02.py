"""
numpy 패키지를 사용한 벡터 연산
"""
import math

import numpy as np

print('numpy version:', np.__version__)

# 두 벡터의 덧셈
v = [1,2] #class list
print(type(v)) #<class 'list'>
print('v =',v)

w = [3,4]
print('w =',w)

print(v + w) # list는 + 연산을 사용할 수 있음 // .extend()와 비슷한 기능
# print(v + w) 새로운 리스트가 생성된다.
# -------------강사님 코멘트
# +연산자는 v나 w를 변경하지 않고, 새로운 리스트를 리턴
# v.extend(w)함수는 v를 변경함
# print(v - w) # 뺄셈은 에러남. // list는 - 연산을 사용할 수 없음!
v.extend(w) # v리스트가 변경된다.
print(v)

# numpy 패키지의 ndarray 타입을 사용
# n-dimensional array(n차원 배열)
v = np.array([1,2])
print(type(v)) # <class 'numpy.ndarray'>
print(v)
print('dimension: ', v.ndim) # v.ndim ==> v가 몇 차원인지

v = np.array([
    [1,2],
    [3,4],
    [5,6]
]) # --> 결과값도 달라지고 type도 바뀐다.
# v1 = np.array([
#     1,
#     [1,2],
#     [3,4]
# ])  #v1은 1차원이다.
print('type: ',type(v))
print('dimension: ', v.ndim) # ==> dimension 2
# shape() 행의갯수, 열의 갯수를 알려준다.
print('shape: ', v.shape) #shape:  (2,) --> 1차원 배열 원소 갯수
# 1차원 ndarray인 경우 shape은 (원소 갯수, )
print('shape: ', v.shape) #shape:  (3, 2) --> 행이 3개 열이 2개
# 2차원 ndarray인 경우 shape는 (row 갯수, column 갯수)
print(v)

# ndarray 타입을 사용한 벡터 연산
v = np.array([1,2,3])
w = np.array([3,4,5])

vector_add = v + w
print('vector add =', vector_add) # vector add = [4 6] 안에 데이터끼리 덧셈 연산을 해준다.
vector_sub = v - w
print('vector sub =', vector_sub)

vectors = np.array([
    [1,2],
    [3,4],
    [5,6]
])

np_sum = np.sum(vectors) # 2차원 배열의 모든 원소들의 합
print('np_sum =',np_sum)

# axis=0: 2차원 배열에서 각 컬럼들의 합으로 이루어진 1차원 배열
np_sum_by_col = np.sum(vectors, axis=0) # axis == 축! axis = 0 은 컬럼 방향 axis = 1 은 행 방향!
print('np_sum_by_col =', np_sum_by_col)  # np_sum_by_col = [4 6]

# axis=1: 2차원 배열에서 각 행(row)들의 합으로 이루어진 1차원 배열
np_sum_by_row = np.sum(vectors, axis=1)
print('np_sum_by_row =', np_sum_by_row )# np_sum_by_row = [ 3  7 11]

np_mean = np.mean(vectors)
print('np_mean =', np_mean)

np_mean_by_col = np.mean(vectors, axis=0)
print('np_mean_by_col =', np_mean_by_col)

np_mean_by_row = np.mean(vectors, axis=1)
print('np_mean_by_row =' , np_mean_by_row)

# 스칼라 곱셈
# v = [1,2,3] # 일반 python의 list이다.
v = np.array([1,2,3])
scalar_mul = 3 * v # 배열의 모든 항목에 3을 곱해라
print('scalar multiplication =', scalar_mul)
# scalar multiplication = [3 6 9]
scalar_div = 3/v #  v / 3
print('scalar_div =', scalar_div)

v = np.array([1,2])
w = np.array([3,4])
print('dot =', v.dot(w)) # 1 *3 + 2*4 dot = 11

# numpy를 사용한 벡터의 크기
def norm(v):
    return math.sqrt(v.dot(v))

v = np.array([1,1])
print('norm =', norm(v))

# numpy를 사용한 두 벡터 간의 거리
def dist(v,w):
    return norm(v-w)
    # return math.sqrt((v - w).dot(v - w))












