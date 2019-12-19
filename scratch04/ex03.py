"""
2차원 리스트를 이용한 행렬
"""
def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 리턴

    :param matrix: n X m 행렬
    (행의 개수가 n개이고 , 열의 개수가 m개인 2차원 리스트)
    :return: tuple(n ,m)
    """
    nrows = len(matrix) # 행의 개수
    ncols = len(matrix[0]) # 열의 개수
    return nrows,ncols

def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴

    :param matrix: n X m 행렬
    :param index: 행 번호
    :return: 벡터( 원소가 m 개인 1차원 리스트)
    """
    return matrix[index]

def get_col(matrix,index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 column을 리턴

    :param matrix: n X m 행렬
    :param index: 행 인덱스
    :return: 벡터(원소가 n개인 1차원 리스트)
    """
    # m = []
    # for i in matrix:
    #     m.append(i[index])

    return [i[index] for i in matrix]

def make_matrix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows X ncols 행렬을 생성

    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수( fn(nrows,ncols) = 숫자)
    :return: nrow X ncols 행렬
    """
    # matrix = [] # 빈 리스트 생성 -> 2차원 리스트
    # for i in range(nrows): # 행의 개수만큼 반복
    #     row = [] # 빈 리스트 생성 -> 행렬에 추가될 행. 1차원 리스트
    #     for j in range(ncols): # 열의 개수만큼 반복
    #        row.append(fn(i,j)) # row에 아이템을 추가
    #     matrix.append(row) # 행렬에 row를 추가
    # return matrix
    return [[fn(i,j) for j in range(ncols) ] for i in range(nrows)] # 윗줄의 코드가 같은 기능을 수행.

# 전치행렬(transpose) : 행과 열을 바꾼다.
def transpose(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼(전치 행렬)을 리턴

    :param matrix: n X m 행렬
    :return: m X n 행렬
    """
    # 강사님 답안 (위에 make_matrix메소드 사용)
    nrows, ncols = shape(matrix)
    t = make_matrix(ncols,nrows,lambda  i,j: matrix[j][i])
    return t

# 위의 transpose와 같은 함수이다 하지만 나중에 나온 함수 transpose가 뒤에 transpose를 덮어버리기
# 때문에 아랫것으로 실행된다.
def transpose(matrix):
    # 내가 작성한 답안
    # m = []
    # for j in range(len(matrix[0])):
    #     row = []
    #     for i in matrix:
    #         row.append(i[j])
    #     m.append(row)
    # return m

    # 강사님답안
    nrows = len(matrix)  # 원본 행렬의 행의 개수
    ncols = len(matrix[0]) # 원본 행렬의 열의 개수
    # t = [] # 전치 행렬
    # for j in range(ncols): # 원본 행렬의 열 개수만큼 반복
    #     원본 행렬의 열(column)을 전치 행렬의 행(row)로 추가
        # t.append(get_col(matrix,j))
    # return t
    return [get_col(matrix,j) for j in range(ncols)]

def transpose(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    # t = []
    # for j in range(ncols):
    #     t_row = [] # 전치 행렬의 행(row)
    #     for i in range(nrows):
    #         t_row.append(matrix[i][j])
    #     t.append(t_row)
    # return t
    # 위의 식을 list comprehension으로 표현하겠다.
    return [[matrix[i][j] for i in range(nrows)]
            for j in range(ncols)]

def transpose(matrix):
    print('unpacking 연산자 *를 사용한 transpose')
    # t = []
    # for col in zip(*matrix):
    #     t.append(list(col))
    # return t
    return [list(x) for x in zip(*matrix)]

if __name__=='__main__':
    # 2 X 3 행렬
    A = [
        [1,2,3],
        [4,5,6]
    ]

    # 3 X 2 행렬
    B = [
        [1,2],
        [3,4],
        [5,6]
    ]

    print(A)
    print(B)

    print('shape of A =' , shape(A)) # (2, 3)
    print('shape of B =' , shape(B)) # (3, 2)

    print(get_row(B,2))
    print(get_col(B,0))

    def plus(x,y):
        return x + y
    m = make_matrix(3,2,lambda x,y: x*y)
    print(m)

    def identity(x,y): # 이것을 make_matrix에 넣으면 항등행렬
        # result = 0
        # if x==y:
        #     result 1
        # else:
        #     result 0
        # result = 1 if x == y else 0 # 3항 연산자
        # return result
        return 1 if x == y else 0

    identity_matrix = make_matrix(3,3,
                                  lambda x,y: 1 if x==y else 0)
    print(identity_matrix)

    print(transpose(A))
    print(transpose(B))

    # zip() 함수를 이용한 전치 행렬
    a = [1,2,3]
    b = [4,5,6]
    c = [7,8,9]
    for x,y,z in zip(a,b,c):
        print(x,y,z)

    # unpacking 연산자: *
    print('A =',A)
    print('*A =',*A)
    print('B =', B)
    print('*B =', *B)







