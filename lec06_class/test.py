def test():
    print('test')

test()

def test(param):
    print('test param =',param)

test()
# java,c++ 등 다른 언어는 overloading을 허용하지만
# python은 overloading을 허용하지 않는다.

# overloading:
# 함수 (메소드)의 파라미터가 다른 경우
# 같은 이름으로 여러개의 함수(메소드)를 정의하는 것
# python은 overloading을 제공하지 않는다!
# 나중에 나오는 이름이 덮어쓴다.

# overriding:
#
#