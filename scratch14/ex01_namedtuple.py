# 번호, 이름, 수학점수, 과학 점수, 컴퓨터점수
from collections import namedtuple
from typing import NamedTuple

student_1 = (1, '홍길동', 10,20,30)
print('번호:', student_1[0])
print('과학점수:', student_1[3])

# 튜플 타입의 단점 :
# - 해당 인덱스의 원소가 무슨 값을 의미하는 지 파악하기 어렵다.
# - 특정 원소에 접근(read/write)하기 위해서는 정수 인덱스만 사용해야 함.

stu_dict = {'no':2,
            'name':'김길동',
            'math':90,
            'science':50,
            'computer':30}

# 튜플의 단점을 해결하기 위해서.
# 튜플의 특징과 딕셔너리(dict)의 특징을 모두 같는 NamedTuple 클래스가 만들어짐
Student = namedtuple('Student',('no','name','math','science','cs'))
student_2 = Student(3,'허균',100,100,100)
print(student_2)
print(f'번호: {student_2[0]}, {student_2.no}')
print(f'수학점수: {student_2.math}')

# Python 3.6 부터 NameTuple을 class 처럼 선언하는 방식이 만들어짐
class Student2(NamedTuple): # Student2 클래스는 NamedTuple 클래스를 상속
    # field 선언 - 변수 타입 annotation을 반드시 추가해야 함.
    no : int
    name : str
    math: int
    science : int
    cs : int

student_3 = Student2(4,'abc',90,88,77) # 클래스는 생성자 호출
print(student_3) # tuple 이기 때문에 인덱스로 접근 가능하다.





