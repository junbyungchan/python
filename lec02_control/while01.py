"""
while 반복문:
[초기식]
while 조건식:
    조건식이 참인 동안에 실행할 문장
    [조건을 변경할 수 있는 식] ---> 생략가능
"""

# 1 2 3 .. 10
n = 1 # 초기값을 설정 해주어야 한다.
while n<10:
    print(n,end=' ')
    n+=1 # n = n + 1 // 조건을 변경할 수 있는 식

print()
# 구구단
dan = 2
while dan<10:
    n =1
    while n<10:
        print(f'{dan} x {n} = {dan*n}')
        if dan == n:
            break
        n+=1
    dan += 1
    print('-----------')
