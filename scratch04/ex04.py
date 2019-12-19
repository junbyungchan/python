"""
numpy의 행렬 관련 함수
"""
import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(A)
print(B)
print(A.shape) # (2, 3) : 2 x 3 행렬   -->    행렬의 모양을 알수있다.
print(B.shape) # (3, 2) : 3 x 2 행렬
nrows, ncols = B.shape
print(nrows,'x',ncols)

# sclicing: 원하는 행, 열의 원소들을 추출
# list[row][col] , ndarray[row,col]
print(A[0,2])
print(A[0,0:2])
print(A[0:2,0:2])
# 모든 행을 뽑아 내겠다
print(A[:,0]) # 인덱스 0번 컬럼의 원소들로 이루어진 array  #숫자 없이 콜론만 쓰자 (:)
# 모든 열을 뽑아 내겠다
print(A[0,:]) # 인덱스 0번 row의 원소들로 이루어진 array


# np.array의 기본 데이터타입은 float이다. int로 표시하려면 dtype=int로 명시해줘야한다.
# 항등 행렬(Identity Matrix) ---- np.identity(n)
identity_matrix = np.identity(3, dtype=int)
print(identity_matrix)

# 전치 행렬(Transpose Matrix) --- A.transpose()
print(A.transpose())
print(B.transpose())

# 행렬의 곱셈 --- A.dot(B)
# 조건 n x m  //  m x k  --->  m의 값이 같아야  n x k 의 행렬이 나온다.
print(A.dot(B))
print(B.dot(A))
