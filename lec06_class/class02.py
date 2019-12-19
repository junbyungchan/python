"""
클래스 = 데이터(필드, field) + 기능(메소드, method) => 데이터 타입
"""


# 클래스 정의
class score:
    # 생성자를 호출했을 때 필드들을 초기화 하는 함수(변수에 값을 저장한다.)
    def __init__(self,korean,english,math):
        # field
        self.korean = korean
        self.english = english
        self.math = math
        # -------------
    # method
    def calc_total(self):
        return self.korean + self.math + self.english

    def calc_avg(self):
        return self.calc_total() / 3
    #----------------------------------------------------

# score 클래스의 객체를 생성해보자
score1 = score(90,80,70) # 생성자 호출
# 컨트롤 키를 누르면 score에 링크가 생긴다.
score1.math = 100
print(score1.calc_total())

score2 = score(90,85,70) # 다른 생성자 호출
print(score2.calc_total())
print(score2.calc_avg())


