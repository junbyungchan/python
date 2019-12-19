"""
파이썬 데이터 타입:
숫자 타입:int(정수),float(실수),complex(복소수)
논리 타입:bool
문자열:str
시퀀스(sequence): list,tuple
매핑(mapping) : dict
집합 : set
None : 값이 없음을 나타내는 데이터 타입
"""
# 숫자형
intVal=123
print(type(intVal))
print(id(intVal)) # 123이라는 메모리는 들고 있는 메모리 주소를 반환해줌.
floatVal=3.141592
print(type(floatVal))

complexVal = 1+2j    # j 는 제곱했을때 마이너스가 되는 값 : 허수를 의미한다.
print(type(complexVal))
print(1j**2)

# bool(논리형)
result = 10<2
print(result)
print(type(result))

# 문자열형
name='abc'
print(type(name))

name= None
print(type(name))