"""
선형 대수(Linear Algebra)
"""
from math import sqrt


def add(v,w):
    """
    주어진 두 개의 벡터에서 성분별로 더하기를 해서,
    새로운 n 차원 벡터를 리턴

    :param v: n차원 벡터(성분이 n 개인 벡터)
    :param w: n차원 벡터(성분이 n 개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    """
    # result = []
    # for i in range(len(v)):
    #     result.append(v[i] + w[i])
    # return result
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함.')
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v,w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 뺄셈을 수행

    :param v: n차원 벡터(성분이 n 개인 벡터)
    :param w: n차원 벡터(성분이 n 개인 벡터)
    :return: 각 성분별로 빼기 결과를 갖는 벡터
    """

    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함.')
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """
    모든 벡터들에서 각 성분별 더하기를 수행
    vector_sum([[1,2],[3,4],[5,6]]) = [9, 12]
    :param vectors: n차원 벡터들의 리스트(2차원 리스트)
    :return: n차원 벡터
    """
    num_of_elements = len(vectors[0])
    for vector in vectors[1:]:
        if num_of_elements != len(vector):
            raise ValueError('모든 벡터는 길이가 같아야 함.')

    # result = [0 for _ in range(num_of_elements)]  # [0, 0, 0 , ...]
    # for i in range(num_of_elements):
    #     for vector in vectors:
    #         result[i] += vector[i]
    # return result

    # 책에 나온 답
    result = vectors[0]
    for vector in vectors[1:]:
        result = add(result,vector)
    return result

def scalar_multiply(c, vector):
    """
    c * [x1,x2,x3,x4,.......] = [c*x1,c*x2,c*x3,......]
    :param c: 숫자(스칼라)
    :param vector: n 차원 벡터
    :return: n차원 벡터
    """
    # result=[]
    # for i in vector:
    #     result.append(c * i)
    # return result

    return [c*i for i in vector]
    # list comprehension 으로 한줄로 코딩 가능하다.

def dot(v,w): # 내적 
    """
    [v1,v2,v3,....] @ [w1,w2,w3,....] = v1*w1 + v2*w2 + v3*w3 +.....

    :param v:n 차원 벡터
    :param w:n 차원 벡터
    :return: 숫자(스칼라)
    """
    if len(v) != len(w):
        raise ValueError('두 벡터의 길이는 같아야 함')
    sum = 0
    for v_i,w_i in zip(v,w):
        sum += v_i * w_i
    return sum

def vector_mean(vectors):
    """
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터

    :param vectors: n차원 벡터들의 리스트
    (길이가 n인 1차원 리스트를 아이템으로 갖는 2차원 리스트)
    :return:
    """
    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))

# 벡터 크기 = sqrt(x1 ** 2 + y1 ** 2)
def sum_of_squares(vector):
    """
    vector = [x1,x2,...., xn] 일 때,
    x1 ** 2 + x2 ** 2 + ... + xn ** 2을 리턴

    :param vector: n 차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    sum = 0
    for i in vector:
        sum += i ** 2
    return sum


def magnitude(vector):
    """
    벡터의 크기를 리턴 - math.sqrt(sum_of_squares)

    :param vector:
    :return:
    """
    return sqrt(sum_of_squares(vector))

def squared_distance(v,w):
    """
    v = [v1,v2,...,vn] , w = [w1,w2,...,wn]일 때,
    (v1 - w1) ** 2 + (v2 - w2) ** 2 + ... + (vn - wn) ++ 2

    :param v: n차원 벡터(길이가 n인 1차원 리스트)
    :param w: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    # sum = 0
    # for i,j in zip(v,w):
    #     sum += (i-j) ** 2
    # return sum
    return sum_of_squares(subtract(v,w))


def distance(v,w):
    """
    두 벡터 v와 w 사이의 거리를 리턴 - sqrt(squared_distance)

    :param v: n차원 벡터(길이가 n인 1차원 리스트)
    :param w: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자자
    """

    return sqrt(squared_distance(v,w))


if __name__ =='__main__':
    v = [1,0,3]
    w = [10,9,2]
    n = [[1,2],[3,4]]
    print('add =',add(v,w))
    print('subtract =',subtract(v,w))
    # 결과값이 이렇게 나온다. zip() 함수때문이다. 벡터의 인덱스가 적은쪽에 맞춰서 결과가 나온다.
    # 좋은 코드가 아니다.
    # [11, 9]
    # [-9, -9]
    # for i in n:
    #     print(i)
    # vectors=[[1,2,3],
    #          [4,5,6],
    #          [7,8,9]]
    # print(vector_sum(vectors))

    sm = scalar_multiply(2, v)
    print('scalar_multiply =' , sm)

    v=[4,4]
    unit_x=[1,0] # x축 단위 벡터
    unit_y=[0,1] # y축 단위 벡터
    dot1 = dot(v,unit_x)
    print('dot1 =',dot1)
    dot2 = dot(v,unit_y)
    print('dot2 =',dot2)

    vectors = [
        [1,2,3],
        [3,4,5],
        [5,6,7],
        [7,8,9]
    ]
    vm = vector_mean(vectors)
    print('vector_mean =',vm)

    v = [3,4]
    w = [3,7]
    ss = sum_of_squares(v)
    print('sum of squares =', ss)
    norm = magnitude(v)
    # norm ==> 벡터의 크기라고 통상 사용한다.
    print('magnitude =', norm)

    v = [1,2]
    w = [3,4]
    sqd = squared_distance(v,w)
    print('squared_distance =',sqd)
    dist = distance(v,w)
    print('distance =', dist)
