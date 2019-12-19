"""
Python 반복문 - for 문
for 변수 in Iterable:
    반복할 문장들

Iterable(반복 가능한 타입들): 리스트,튜플,세트(집합),딕셔너리,문자열,...
"""

# range(to) : 0부터 (to - 1) 까지 범위의 숫자들
# range(from, to) : from 부터 (to - 1) 까지 범위의 숫자들
# range(from, to, step) : from 부터 (to -1) 까지 step만큼 씩 증가 또는 감소
# 파이썬에서는 끝자리 숫자는 포함하지 말자.
for i in range(5): # ( 0, 1, 2, 3, 4)
    print(i, end=' ') # end=' ' 출력시에  줄바꿈을 하지 말라
print()

for i in range(1,5): # (1,2,3,4)
    print(i,end=' ')
print()

for i in range(1,5,2): # (1,3)
    print(i,end=' ')
print()
for s in 'Hello, Python!':
    print(s,end='')
print()

languages = ['PL/SQL','R','Python','Java','C'] # 리스트도 가능
for lang in languages:
    print(lang, end=' ')
print()

for i in range(len(languages)):
    print(i, languages[i])
print()

# 딕셔너리를 for문 돌리기
alphabet = {1:'a',2:'b',3:'c'}
print(alphabet.keys()) # dict의 키(key)들
for key in alphabet.keys():
    print(key,alphabet[key])

# in dict는 딕셔너리의 key들을 반복!!!!
for key in alphabet:
    print(key)

for item in alphabet.items():
    print(item) # 튜플을 반환해준다.

# key, value = (1, 'a')
for key,value in alphabet.items():
    print(key,value)