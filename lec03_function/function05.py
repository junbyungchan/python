"""
가변 길이 인수(variable-Length argument)
함수를 호출할 대 전달하는 argument의 갯수가 변할 수 있을 때
사용하는 방식
파라미터 이름 앞에 *를 붙임.
"""

print('a')
print('a','b','c','d')

def fn_vararg(*varargs):
    print(varargs)
    print(*varargs)
    # 가변길이 인수들은 tuple처럼 취급하면 됨
    for arg in varargs:
        print(arg)

fn_vararg(1,2)

def summation(*args):
    """
    임의의 갯수의 숫자들을 전달받아서 그 숫자들의 총합을 리턴하는 함수

    :param args: 합계를 계산할 숫자들(갯수 제한 없음)
    :return: 숫자들의 합
    """
    total = 0
    for arg in args: # 튜플처럼 생각하면 된다.
        total += arg
    return total

a = summation(1,2,3,4,5,6)
print(a)
print(summation()) # 결과값이 0이다 error가 나는것도 아니다

def fn_vararg2(a,*b): # 가변길이 인수에는 파라미터를 주지 않아도 빈 튜플로 반환을 해준다.
    print(f'a = {a}')
    print(f'b = {b}')

# fn_vararg2() ---> a값을 전달하지 않으면 에러 발생
fn_vararg2(1) # b는 가변길이 파라미터이므로 인수를 전달하지 않아도 된다.

def fn_varargs3(*a,b):
    print(f'a={a}')
    print(f'b={b}')

# fn_varargs3()
# fn_varargs3(1)
# fn_varargs3(1,2) a가 1,2를 모두 가져가버리기 때문에 b에 전달될 파라미터가 없다.
fn_varargs3(1,b=1) # keyword방식으로만 해야지 오류가 나지않고 b에 파라미터가 전달될수 있다.
# 가변길이 파라미터 뒤에 선언된 파라미터에 값을 전달할 때는
# keyword 방식으로만 값(argument)를 전달할 수 있음

def calculator(*values,operator):
    """
    operator가 '+'인 경우에는 모든 values들의 모든 합계를 리턴하고,
    operator가 '*'인 경우에는 모든 values들의 모든 곱을 리턴하는 함수
    operator가 '+','*'가 아니면 None을 리턴
    :param values:
    :param operator:
    :return:
    """
    result = None
    if operator =='+':
        total = 0
        for n in values:
            total += n
        return total
    elif operator=='*':
        tot = 1
        for n in values:
            tot*=n
        return tot
print(calculator(100,20,30,40,operator='*'))










