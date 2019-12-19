"""
명시적 형 변환(casting) : int(), float(), str()
"""
# print('3.1' + 1.2) # typeError가 난다.
# 문자열(str)과 숫자(float)은 산술 연산을 할 수 없음.
# 숫자 타입으로 변환 후 산술 연산을 실행.
print(float('3.1') + 1.2)
# 문자열 + 문자열 : concatenate(문자열 이어 붙이기)
print('3.1' + str(1.2))

x = input('>>> 숫자(x) 입력:')
y = input('>>> 숫자(y) 입력:')
# input으로 받는 x,y는 문자열로 저장되어있는다. 그래서 int(x) , int(y) 로 형 변환을 해주어야 계산이 가능하다.
x = float(x)
y = float(y)
print(f'{x}+{y} = {x+y}')
print(f'{x}-{y} = {x-y}')
print(f'{x}*{y} = {x*y}')
print(f'{x}/{y} = {x/y}')
# Ctrl + D : 커서가 있는 줄을 복사&붙여 넣기