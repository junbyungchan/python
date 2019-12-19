"""
함수 (function): 기능을 수행해서 값을 반환(return)하는 코드 블록
인수 (argument): 함수를 호출할 때 전달하는 값
매개변수 (parameter): argument를 저장하기 위해서, 함수를 정의할 때 선언하는 변수
"""

# 형식 : 함수(인수)
print('Hello , World') # 함수 호출(call, invoke), argument 1개
# print 함수는 return을 하지 않는다. 이런 함수도 있다.

print() # argument 0개
print('hello','pyhton',123) # argument 3개

print('hello',end=',') # end의 기본값은 줄을 바꿔주는것이다.
print('python')


# Python 내장(built-in) 함수들
# Ctrl + Q : 함수/클래스 문서(documentation) 보기
result = sum([1,2,3,4,5])
# result : 함수 sum의 리턴 값(반환 값)
print(result)

result = abs(-5)
print(result)

result = pow(2,4)
print(result)

result = pow(2,4,3) # ----> 2 ** 4 % 3 = 16 % 3 = 나머지 : 1
print(result)



