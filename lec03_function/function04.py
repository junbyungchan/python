# 함수 정의
def test(x,y):
    print(f'x = {x}, y ={y}')
    return x+y,x-y


# 함수 호출
# test()
# 실행 중에 TypeError 발생
# 파이썬은 함수의 파라미터 타입은 검사하지 않지만,
# 파라미터 갯수는 검사를 합니다.
# positional argument : 함수를 호출할 때 전달하는 값(argument)들이
# 함수 정의에 선언된 파라미터 순서대로 전달되는 방식
plus , minus = test(1,2)
plus , minus = test(2,1)

# keyword argument: 함수를 호출할 때, argument를
# 파라미터=값 형식으로 전달하는 방식
# keyword argument를 사용하면 함수에 정의된 파라미터 순서와
# 상관 없이 argument를 전달할 수 있다.
plus, minus = test(x=10,y=20)
print(minus)

plus , minus = test(y=20,x=10)
print(minus)

# default argument: 함수를 정의할때
# 파라미터의 기본값을 설정하는 것
def show_msg(msg: str = 'hello', times: int = 1) -> None:
    print(msg * times)

show_msg('졸리세요?',10)
show_msg('넵 많이 졸리네요 ')
show_msg()

# default argument를 갖는 파라미터는
# default argument를 갖지 않는 파라미터들이 선언된 뒤에
# 선언해야함함# def test2(x =1, y ):
#     return x +y

