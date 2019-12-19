"""
함수 정의:
def 함수이름(파라미터: 타입, 파라미터2: 타입, ...) -> 리턴타입:
    함수 기능(body)
"""


def subtract(x: int,y: int) -> int:
    return x - y

result = subtract(5,3)
print(result)

# 파이썬은 함수를 호출할 때
# 함수 파라미터 타입과 리턴 타입을 검사하지 않음!
result = subtract(1.1, 0.9)
print(result)


def my_sum(numbers: list) -> float:
    """
    숫자(int,float)들이 저장된 리스트를 전달받아서 ,
    모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 합
    """
    total = 0
    for i in numbers:
        total += i
    return total

a = [1,2,3,4,5]
print(my_sum(a))

def my_mean(numbers: list) -> float:
    """
    숫자들을 저장하는 리스트를 전달받아서,
    모든 원소들의 평균을 계산해서 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 평균
    """

    total = 0
    for i in numbers:
        total += i
    avg = total/len(numbers)
    return avg
    # 간단하게 사용해보자
    # return my_sum(numbers)/len(numbers) --> 이 한문장이면 끝이다.

a = my_mean([915,123,483,154])
print(a)

# Ctrl 키를 누르고 함수 위에 마우스로 클릭하면 그 함수가 정의되어 있는
# 부분으로 간다.







