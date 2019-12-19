"""
재귀 함수(recursive function)
"""

# factorial
# 0! = 1
# n! = 1 x 2 x 3 x 4 .... x (n-1) x n = (n-1)! x n

def factorial1(n : int)->int:
    result = 1
    if n >= 0:
        for i in range(1, n+1):
            result *= i # result = result * i

    return result
def factorial2(n : int)->int:
    if n == 0:
        return 1
    elif n > 0:
        return factorial2(n-1) * n

for n in range(1,6):
    print(f' {n}!:{factorial1(n)}')
print('=========')
for n in range(1,6):
    print(f' {n}!:{factorial2(n)}')

# 하노이의 탑
print('=========================')
def hanoi(n,start,target,sub):
    if n == 1 :
        print(start,'->',target)
        return
    else:
        hanoi(n-1,start,sub,target)
        print(start,'->',target)
        hanoi(n-1,sub,target,start)
        return

print(hanoi(2,'시작','끝','중간'))

