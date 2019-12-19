"""
여러가지 print() 방법
"""

print('Hello, python!')

age = 16
name = '오쌤'
print('나이:',age,', 이름:',name)
# age와 쉼표 사이의 공백은 없앨수가 없다.
print(f'나이:{age},이름:{name}') # formatted string 포맷을 만든 문자열
print('나이:{},이름:{}'.format(age,name))  # formatted string의 한 종류
print('나이: %d, 이름: %s' %(age,name))
# %d: 정수 , %f : 실수 , %s : 문자열
# digit  , floating-point , string
"""
사용자 입력(키보드 입력) 처리 
"""
print('>>> 이름을 입력하세요:')
name = input()
print(f'name:{name}')

age = input('>>> 나이 입력:')
print(f'age:{age}') # 콘솔 창에서 입력한 값들은 문자열이므로 산수가 불가능하다.
# print(age +1) # 실행 중 오류(Type Error) 발생
# Ctrl + / : 주석 토글