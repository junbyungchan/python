"""
가위(1)/바위(2)/보(3)
"""
import numpy as np
# numpy라는 패키지를 사용하겠다. 줄여서 np라고 표현하겠다.

print('가위바위보 게임')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('----------------------')
print('선택 >>>')

user = int(input())

computer = np.random.randint(1,4) # (1,4)라고 쓴 [이유 1보다는 크거나 같고 4보다 작은 난수 발생 ]
print(computer)
# 1 : 가위 2 : 바위 3 : 보
if user == computer:
    print('비겼습니다.')
elif user == 1 and computer == 2:
    print('user 패배!')
    print('computer 승리!')
elif user == 1 and computer == 3:
    print('user 승리!')
    print('computer 패배!')
elif user == 2 and computer == 1:
    print('user 승리!')
    print('computer 패배!')
elif user == 2 and computer == 3:
    print('user 패배!')
    print('computer 승리!')
elif user == 3 and computer == 1:
    print('user 패배!')
    print('computer 승리!')
elif user == 3 and computer == 2:
    print('user 승리!')
    print('computer 패배!')

result = user - computer
if result == 0: # 비김
    pass
elif result ==1 or result ==2: # user
    pass
else:
    pass
