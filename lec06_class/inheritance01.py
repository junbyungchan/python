"""
상속(inheritance):
부모 클래스로부터 데이터(field)와 기능(method)를 물려받아서
자식 클래스에서 사용할 수 있도록 하는 개념
- parent(부모), super(상위), base(기본) class
- child(자식), sub(하위), derived(유도) class
"""
from math import pi
# 모든 class의 조상은 object이다.
# 그래서 생략이 가능하다.
# class Shape(object): --> 원래 이 표현인데 생략을 한다.
class Shape:
    def __init__(self,x=0,y=0):
        print('Shape __init__ 호출')
        self.x = x
        self.y = y


    def __repr__(self):
        return f'Shape(x={self.x},y={self.y})'

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    # 면적 계산하는 메소드
    def area(self):
        """
        # Shape 객체는 넓이를 계산할 수 없고,
        # Shape의 sub 타입들인 Rectangle, Circle 객체가
        # 각자의 방식으로 넓이를 계산해야 됨.

        :return: 도형의 넓이
        """
        raise NotImplementedError('반드시 override')


    def draw(self):
        """
        넓이를 계산하는 area() 메소드를 사용해서 도형 내부를
        그려주는 메소드

        :return: None
        """
        print(f'Drawing {self.area()}....')





# 상속:
# class child명(parent명):
#   class의 body
class Rectangle(Shape):
    # Child 클래스에서 __init__ 메소드를 작성하지 않은 경우에는
    # 파이썬 인터프리터가 Parent 클래스의 __init__ 메소드를
    # 호출해서 부모 객체를 자동으로 생성함.
    # 개발자가 Child 클래스에서 __init__ 메소드를 정의한 경우에는
    # 파이썬 인터프리터가 Parent 클래스의 __init__ 메소드를
    # 자동으로 호출하지 않음.
    # child 클래스에서 parent 클래스의 __init__ 메소드를 명시적으로 반드시 호출해야함!
    def __init__(self,w,h,x=0,y=0): # child의 __init__ 메소드는 4개
        print('Rectangle.__init__ 호출')
        super().__init__(x,y) # 부모클래스의 __init__호출
        self.w = w
        self.h = h


    #override : 부모 클래스로부터 상속받은 메소드를
    # 자식 클래스에서 재정의하는 것
    def __repr__(self):
        # 부모의 class 있는 __repr__의 메소드 위에
        # 자식의 class 있는 __repr__의 메소드를 덮어 씌운다.
        return f'사각형 (가로:{self.w} / 세로: {self.h} / x:{self.x} / y:{self.y})'
        # super() ---> 부모의 주소.__intit__)
    # child 에서 init을 명시하면 parent의 init을 자동으로 호출해주지 않는다.

    def area(self): # Shape 클래스에도 area() 메소드가 있지만
                    # override를 사용해서 덮어쓰기를 해서 area()를 오버라이드했다.
        return self.w * self.h

class Circle(Shape):
# class Circle(Shape, object): ---> 다중상속

    def __init__(self,r,x,y): # r: 원의 반지금 , (x,y) : 원의 중심의 좌표
        print('Circle.__init__ 호출') # 함수 호출 순서를 보기위한 출력문
        # super 클래스의 __init__ 메소드를 반드시(!) 호출해야 함.
        super().__init__(x,y) # 부모 클래스의 __init__ 호출
        # Shape.__init__(self,x,y)  super().__init__()과 같은 코드이지만
        # 클래스이름.__init__(self) 파라미터에서 self를 반드시 명시해줘야한다. # self 생략 불가
        # sub 클래스만 갖는 field를 초기화
        self.r = r # 반지름 초기화

    def __repr__(self):
        return f'( Circle: 반지름 :{self.r} / 중심점 좌표: ({self.x},{self.y}) )'

    def area(self):
        return (self.r **2) * pi



if __name__ == '__main__': # test 코드를 만드는 이유
    # 다른 클래스에서 import 할때 다른 클래스에서도 실행되지 않게 하기 위해서
    shape1 = Shape(0,0)
    print(shape1)
    shape1.move(1,2)
    print(shape1)

    rect1 = Rectangle(w=3,h=4,x=0,y=0)
    print('rect1 타입:' , type(rect1))
    print('rect1:',rect1) # override한 __repr__ 메소드가 호출됨.
    rect1.move(-1,-2) # 부모에게서 상송받은 move 메소드가 호출됨.
    print(rect1)

    print('---------------------------')

    circle1 = Circle(r=5,x=8,y=10)
    print('circle1 type: ', type(circle1))
    print(circle1)

    rect1.draw()
    circle1.draw()






