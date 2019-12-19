"""
for-in 구문 연습
"""

# 구구단 2단부터 9단까지 출력

x = int(input('몇단이 궁금? >>>'))

for i in range(x,x+1):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print('------')

# 구구단 2단은 2*2 까지만 3단은 3*3 까지만  4단은 4*4 까지

for i in range(2,10):
    for j in range(1,i+1):
        print(f'{i} x {j} = {i*j}')
    print('------')

# 다른 방법
for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan} x {n} = {dan*n}')
        if dan == n :
            break # break가 포함된 가장 가까운 반복문을 종료
    print('------------')

# continue / break

for i in range(1,10):
    if i == 5:
        continue # continue 밑으로 내려가지 않고 다시 위의 반복문으로 올라가겠다. (반복문의 처음 부분으로 이동해서 계속 실행)
       #break 반복문을 종료하겠다.
    print(i,end=' ')
print()