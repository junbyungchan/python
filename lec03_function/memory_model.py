"""
파이썬 메모리 모델 -
파이썬이 변수들의 메모리 공간을 관리하는 방법
"""

n1 = 1
print(f'주소 = {id(n1)} , 저장된 값 = {n1}')

n2 = n1
print(f'주소 = {id(n2)}, 저장된 값 = {n2}')

n2 = 2
print(f'주소 = {id(n2)}, 저장된 값 = {n2}')

n3 = 1
print(f'주소 = {id(n3)}, 저장된 값 = {n3}')
# 숫자와 문자열인 경우에
# 생성된 객체를 캐싱함(재활용).

n3 = 3-1 # n2의 주소와 같다.
print(f'주소 = {id(n3)}, 저장된 값 = {n3}')

# 숫자와 문자열을 제외한 다른 모든 객체들은 값이 사용할 때마다 새로 생성됨
f1 = 1.20
print(f'주소 = {id(f1)}, 저장된 값 = {f1}')
f2 = 1.2
print(f'주소 = {id(f2)}, 저장된 값 = {f2}')

s1 = 'abc'
print(f'주소 = {id(s1)}, 저장된 값 = {s1}')
s2 = 'abc'
print(f'주소 = {id(s2)}, 저장된 값 = {s2}')

list1 = [1,2,3]
print(f'주소 = {id(list1)}, 저장된 값 = {list1}')
list2 = [1,2,3] # 기존 리스트를 재활용하지 않고, 새로운 리스트 생성
print(f'주소 = {id(list2)}, 저장된 값 = {list2}')
list2[0] = 100
print(list1) # list1 에는 영향 없음
print(list2)

list3 = list2
print(f'주소 = {id(list3)}, 저장된 값 = {list3}')
list3[1] = 200
print(list2,list3)

bool1 = True
print(f'주소 = {id(bool1)}, 저장된 값 = {bool1}')
bool2 = False
print(f'주소 = {id(bool2)}, 저장된 값 = {bool2}')
print('=========================================')
# == 연산자 VS is 연산자
# == 연산자는 a 와 b 의 값들을 비교함 / 두 변수가 참조하는 객체의 값이 같은지 비교
# is 연산자는 a 와 b 의 id, 즉 주소를 비교함 / 두 변수에 저장된 주소를 비교
a = [1,2,3]
b = [1,2,3]
print(f'==:{a==b}, is:{a is b}')




