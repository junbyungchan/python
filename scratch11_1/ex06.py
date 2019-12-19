# Iterable: for~ in 구문에서 사용할 수 있는 타입들
# list, tuple, set, dict, numpy.ndarray, pandas.DataFrame, ...
# for x in list: ...

a = [1,3,0,9,-1]
result = sorted(a, key = lambda x: abs(x), reverse=True)
# key = 의 리턴값을 기준으로 sort한다.
# 람다 = 람다 x를 주면 : f(x)를 주겠습니다.
print(f'a={a}, result {result}')
result = a.sort()
print(f'a={a}, result ={result}')

b = ['cat','bb','dogs','apples']
result = sorted(b, key= lambda x: len(x) ) # result = ['bb', 'cat', 'dogs', 'apples'] len(x)의 길이를 기준으로 구한다.
print(f'a={b} , result = {result}')

c = {'cat':1,'bb':-1, 'dogs':3,'apple':5}
for x in c.items(): # key 값들만 뽑아 내준다. 기억하자. 같은 의미로 for x in c.keys():
    print(x)        # for x in c.items(): ---> 키와 값을 튜플형태로 출력해준다.

result = sorted(c) #  dict의 키들만 정렬한 리스트  result=['apple', 'bb', 'cat', 'dogs']
                   # a,b,c,d의 순서로 정렬했다.
print(f'c={c} , result={result}')

result = sorted(c, key = lambda  x: len(x)) # dict의 키들만 정렬한 리스트
print(f'c={c}, result = {result}')

result = sorted(c.values(), key=lambda  x: abs(x)) # dict의 value들만 정렬한 리스트
print(f'c={c}, result = {result}')

result = sorted(c.items(), key=lambda  x:x[1]) # dict의 (key,value)를 정렬한 리스트
print(f'c={c}, result = {result}')

class Person:
    def __init__(self, name : str ,age : int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(이름 : {self.name}, 나이 : {self.age})'

p1 = Person('이지수', 10) # 생성자 호출
print(p1.name, p1.age) # f(field), property(특성, 속성), member variable(멤버 변수)
p2 = Person('심진섭', 20)
p3 = Person('조성우', 30)
persons = [p1,p2,p3] # Person 클래스 객체들의 리스트
print(persons) # class 안에서 __repr__ 를 만들어 줘서 프린트문 변경

result = sorted(persons, key= lambda x: x.name) # x => p1 , p2 , p3 가 된다.
print(result)





