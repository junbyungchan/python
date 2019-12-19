"""
선택 정렬 알고리즘
"""
import numpy as np

def find_min(numbers : list,reverse):
    """
    주어진 리스트에서 최솟값과 최솟값의 인덱스를 찾아서 리턴

    :param numbers: 숫자들의 리스트
    :return: (최솟값의 인덱스, 최솟값)의 쌍(tuple)
    """
    if reverse is True:
        min_id, min_value = 0, numbers[0]
        for i,v in enumerate(numbers):
            if v > min_value:
                min_id, min_value = i,v
        return min_id, min_value
    elif reverse is False:
        min_id, min_value = 0, numbers[0]
        for i, v in enumerate(numbers):
            if v < min_value:
                min_id, min_value = i, v
        return min_id, min_value

def sel_sort(numbers: list,reverse=False ):
    """
    주어진 리스트의 원소들이 정렬된 새로운 리스트를 생성해서 리턴
    주어진 리스트(파라미터에 전달된 리스트)의 순서는 바뀌지 않음

    :param numbers:
    :param reverse: FALSE인 경우는 오름차순 , TRUE인 경우는 내림차순
    기본값은 FALSE
    :return:
    """
    result = [] # 빈 리스트 생성

    while numbers: # numbers의 원소가 있는 동안에
        print('numbers:', numbers)
        print('result:', result)
        _, min_value = find_min(numbers,reverse) # 최솟값을 찾음
        result.append(min_value) # 결과 리스트에 추가
        numbers.remove(min_value)
    return result

numbers = [np.random.randint(0,101) for i in range(10)]
sorted_numbers = sel_sort(numbers)
print('sorted_numbers =', sorted_numbers)

print('================================================')
def sel_sort2(numbers : list , reverse=False) -> None:
    """
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고, 워논 리스트의 순서를 바꿈

    :param numbers:
    :return: reverse: FALSE 이면 오름차순, TRUE 이면 내림차순 정렬.
    기본값은 FALSE(오름차순 정렬)
    """

    length = len(numbers)
    if reverse == False:
        for i in range(0,length-1):
            # i : 최솟값을 옮길 위치
            for j in range(i+1,length):
                # j : 최솟값을 찾기 위해서 비교할 원소들의 인덱스
                if numbers[i] > numbers[j]:
                    numbers[i] , numbers[j] = numbers[j] ,numbers[i]

    elif reverse == True:
        for i in range(0,length-1):
            for j in range(i+1,length):
                if numbers[i] < numbers[j]:
                    numbers[i] , numbers[j] = numbers[j] , numbers[i]

numbers = [np.random.randint(0,101) for x in range(10)]
print(numbers)
sel_sort2(numbers, reverse=True)
print(numbers)





