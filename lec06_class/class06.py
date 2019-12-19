import math

class Circle:
    # field: 반지름(radius)
    # method:
    # __init__() : 초기화 함수(객체 생성 함수)
    # area(): 원의 넓이를 리턴
    # perimeter(): 원의 둘레 길이를 리턴
    # __str__(): Circle(r=123) 형식으로 출력
    # __eq__(): 반지름이 같으면 equal
    def __init__(self,radius):

        self.radius = radius
        if self.radius < 0:
            raise ValueError('반지름은 0 또는 양수')
    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi

    def __str__(self): # print할 때 자동으로 호출되는 함수이다!
        return f'<Circle(r={self.radius})>'

    # representation
    def __repr__(self): # __str__ 과 비슷한 함수
        # 리스트나 딕셔너리, Set 안의 있는 객체들을 print표현식
        return f'원({self.radius})'

    def __eq__(self, other):
         print('__eq__ 호출')
         return self.radius == other.radius

    def __ne__(self, other): # not equal
        # != 연산자를 사용하면 자동으로 호출되는 메소드
        print('__ne__호출')
        return self.radius == other.radius

    def __gt__(self, other):
        # greater than: > 연산자를 사용하면 자동으로 호출
        print('__gt__ 호출')
        return self.radius > other.radius

    def __ge__(self, other):
        # greater than or equal to
        # >= 연산자를 사용하면 자동으로 호출되는 메소드
        #return self.__gt__(other) or self.__eq__(other)
        return self.radius >= other.radius

    # __lt__ : less than(<)
    # __lte__ : less than or equal to (<=)







if __name__ == '__main__':
    c1 = Circle(3)
    print(c1)
    print(f'c1의 넓이는 {c1.area()}입니다.')
    print(f'c1의 둘레는 {c1.perimeter()}입니다.')
    print('c1 id:', id(c1)) # 생성된 객체의 주소

    c2 = Circle(3)
    print(c2)
    print(f'c2의 넓이는 {c2.area()}입니다.')
    print(f'c2의 둘레는 {c2.perimeter()}입니다.')
    print('c2 id:', id(c2)) # 생성된 객체의 주소

    print(c1 == c2)  # c1.__eq__(c2)
    print(c1 != c2)  # c1.__ne__(c2)
    # __eq__ 메소드만 작성한 경우,
    # != 연산자는 __eq__ 메소드를 호출한 후 그 결과값의 반대(not)를 사용
    # __ne__ 메소드가 있는 경우,
    # != 연산자는 __ne__ 메소드의 리턴 값을 사용

    print(c1 > c2) # c1.__gt__(c2)
    print(c1 >= c2)
    print(c1 < c2)
    print(c1 <= c2)

    circles = [
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(0),
        Circle(50)
    ]
    print(circles)
    print('------------------')
    print(sorted(circles)) # 오름차순 정렬
    print(sorted(circles,reverse=True)) # 내림차순 정렬







