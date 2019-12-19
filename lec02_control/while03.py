"""
반복문 연습
Shift + F6 ---> Refactor/Rename
"""

# 1 + 2+ 3 + 4 + 5 + .... + 100 = ?

n , total = 1 , 0 # ---> 변수 저장 이렇게도 가능하다.
while n<=100:
    total += n
    n += 1
print(total)

# 1 + 2 + 3 + ... + x <= 100

tot = 0
k = 0
while True:
    k += 1
    tot += k
    if tot+k > 100:
        break
print(k)

# 책 예제 p.230
# 13번
for i in range(1,8):
    for j in range(1,i+1):
        print('T',end='')
    print()

# 14번
for i in range(1,8):
    for j in range(1,8-i):
        print(' ',end='')
    for j in range(1,i+1):
        print('T',end='')
    print()
# 15번 - 1
i=1
while i<8:
    j=1
    while j<i+1:

        print('T',end='')
        j += 1
    i +=1
    print()

# 15번 - 2


