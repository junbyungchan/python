"""
gradient descent 연습
"""
import random

import matplotlib.pyplot as plt
from scratch08.ex01 import difference_quotient,move



def g(x):
    """ y = (1/3)x ** 3 - x"""
    return x ** 3 / 3 - x




if __name__ == '__main__':
    # ex01에서 작성한 함수들을 이용
    # 함수 g(x)의 그래프를 그림
    # 극값(local 최소/최대)를 경사 하강법으로 찾음
    xs = [x /10 for x in range(-30,31)]
    ys = [g(x) for x in xs]

    plt.plot(xs,ys)
    plt.axvline(x=0, color = 'black')
    plt.axhline(y=0, color = 'black')
    plt.axvline(x=1, color = '0.75')
    plt.axvline(x=-1, color = '0.75')
    plt.ylim(bottom = -2, top = 2)
    plt.title('y = x ** 3 / 3 - x')
    plt.show()

    # 극값(Local 최소/ 최대)를 경사 하강법으로 찾음
    tolerance = 0.0000001
    # 극소(지역) 최솟값을 찾기 위한 x 시작 좌표
    init_x = 1.9
    count = 0
    while True: # 반복
        count += 1
        # x 좌표 init_x 에서의 접선의 기울기를 찾는다.
        gradient = difference_quotient(g,init_x , h = 0.001)
        # x 좌표를 이동: 최솟값 문제이기 때문에 기울기 반대 방향
        next_x = move(init_x,gradient,step= -0.2)
        print(f'{count}: x= {next_x}')
        # 이동 전후의 x좌표 사이의 거리가 tolerance(임계값) 보다
        # 작은지를 확인. 만약 임계값보다 작다면 반복 종료
        if abs(next_x - init_x) < tolerance:
            break
        else:
            # 이동 후의 x의 위치를 새로운 기울기를 찾기 위한 시작 값으로
            init_x = next_x


    # 최댓값을 찾기 위한 x 시작위치
    init_x = -1.9
    count = 0
    while True: # 반복
        count += 1
        gradient = difference_quotient(g,init_x, h =0.001)
        next_x = move(init_x,gradient,step= 0.2)
        print(f'{count}: x= {next_x}')

        if abs(next_x - init_x) < tolerance:
            break
        else:
            init_x = next_x
    ## 위의 두개의 코드들은 거의 같으므로 함수로 만들어서 사용하면 재사용성이 좋다.