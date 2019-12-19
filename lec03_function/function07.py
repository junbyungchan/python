"""
연습문제1
1부터 n까지의 숫자들의 합을 리턴하는 함수
1 + 2 + 3 + 4 + 5 + 6 + ... + n

연습문제2
1부터 n까지의 숫자들의 제곱의 합을 리턴하는 함수
1 **2 + 2**2+3**2+4**2+ .... n**2
 ---> 공식  (n*(n+1)*(2n+1)) /6

연습문제3
숫자들의 리스트를 전달받아서 최댓값을 찾아서 리턴하는 함수

연습문제4
숫자들의 리스트를 전달받아서 최댓값의 인덱스를 리턴하는 함수

연습문제5
숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수
"""
import math



# 연습문제 1
def sum_n(x):
    tot = 0
    for i in range(x+1):
        tot += i
    return tot

print(sum_n(10))

# 강사님 답
# def sum_to_n3(n: int ) -> int:
#     numbers = [x for x in range(1,n+1)]
#     print(numbers)
#     return sum(numbers)
# print(sum_to_n3(10))


# 연습문제 2
def sum_pow_n(x):
    tot = 0
    for i in range(x+1):
        tot += i**2
    return tot

print(sum_pow_n(10))

# 강사님 답
# def sum_to_squares(n:int) -> float:
#     return (n*(n+1)*(2*n+1)) /6
#
# def sum_to_squares2(n:int) -> int:
#     _sum=0
#     for x in range(1,n+1):
#         _sum += x ** 2
#     return _sum
# print(sum_to_squares(3))
# print(sum_to_squares2(3))

# 연습문제 3
def max_find(x : list):
    max = 0
    for i in x:
        if i > max:
            max=i
    return max

print(max_find([1,2,3,4,5,6,7]))

# 강사님 답
# def find_max(values: list) -> float:
#     # return max(values) # 내장함수가 있음.
#     _max = values[0]
#     # 값 사용 방법
#     # for x in values:
#     #     if x > _max:
#     #         _max = x
#     # return _max
#
#     # 인덱스 사용 방법
#     # for i in range(1, len(values)):
#     #     if values[i] > _max:
#     #         _max = values[i]
#     # return _max
# print(find_max([1,2,100,99,1000,0]))
#
# def find_max2(values : list) -> float:
#     # sorted(list) : list를 정렬한 새로운 리스트 리턴
#     # 원본 리스트(list)는 순서가 그대로 유지됨
#     # list.sort(): 원본 리스트를 정렬해서 순서를 바꿈.
#     # None을 리턴함(값을 리턴하지 않음)
#     sorted_values = sorted(values, reverse=True)
#     print('values:', values)
#     print('sorted_values:', sorted_values)
#     # return sorted_values[0]
#     values.sort(reverse=True) # list.sort()를 저장하면 전에 있던 list는 사라지니 조심하자.
#     print('values:',values)
#     return values[0]
#
# numbers = [1,2,3,1000,152,1436,12345667]
# find_max2(numbers)

# 연습문제 4
def max_index_find(x :list):
    max = 0
    for i in x:
        if i > max:
            max = i


    return x.index(max)

print(max_index_find([7,8,0,3,110,1,2,3]))

# 강사님 답
# def find_max_index(values : list)->float:
#     max_id,max_val = 0 , values[0]
#     for i,v in enumerate(values): # enumerate(list)를 주면 i 값으로 인덱스 값을, v 값으로 인덱스에 해당하는 값을 반환해준다.
#         print(f'i:{i},v:{v}')
#         # 출력값 i : 인덱스값  , v : 값
#         if v > max_val:
#             max_id , max_val = i , v
#     return max_id
# numbers = [90,89,70,99,58]
# print(find_max_index(numbers))
#
# def find_max_index2(values):
#     _max = values[0]
#     for i in range(1,len(values)):
#         if values[i] > _max:
#             max_id = i
#     return max_id

# def find_max_index3(values):
#     max_id , _max = 0, values[0]
#     idx = 0
#     for x in values:
#         if x > _max:
#             max_id , _max = idx ,x
#         idx += 1
#     return max_id

# 연습문제 5
def middle_find(x : list):
    y=sorted(x)
    n = len(x)
    if n % 2 == 0: # 짝수다
        middle = (y[int(n/2) -1] + y[int(n/2)]) / 2

    elif n % 2 == 1: # 홀수다
        middle = y[math.floor(n/2+1) -1]

    return middle

print(middle_find([7,4,8,0,1,10]))

# 강사님 답
# def median(values : list) -> float:
#     # 리스트를 정렬(내림차순)
#     sorted_values = sorted(values)
#     length = len(sorted_values) # 리스트의 크기
#     mid = length//2 # 리스트의 중간 위치
#     if length % 2: # 리스트의 원소 갯수가 홀수인 경우
#         median_values = sorted_values[mid]
#     else: # 리스트의 원소의 갯수가 짝수인 경우
#         left = mid - 1
#         median_value = (sorted_values[left] +
#                         sorted_values[mid]) / 2
#     return median_value
