"""
for-in 구문 연습
"""

# 피보나치 수열(fibonacci sequence)
# f[0] = 0 , f[1] = 1
# f[n] = f[n-1] + f[n-2] , n>=2
f = [0,1]

for i in range(2,20):
    # f[i] = f[i-1] + f[i-2] 이렇게 작성하면 out of index 가 뜬다.
    # f[2]는 아직 생성되지 않았기 때문이다.
    f.append(f[i-1] + f[i-2])

# for i in range(0,18):
#     f.append(f[n+1] + f[n])
print(f)

# 소수(prime number): 1과 자기자신으로만 나누어지는 정수
# 2부터 10까지의 정수들 중에서 소수를 찾아서 출력
a =[]
for i in range(2,11):
    sw = True
    for j in range(2,i):
        if i % j == 0: # 약수가 존재한다
            print(f'{i} = {j} x {i/j}')
            sw = False # 소수가 아니라고 표시
            break

    if sw: # sw 가 true일 때 아래 문장이 실행
        a.append(i)
print(a)

# for/while 반복문과 else가 함께 사용되는 경우:
# 반복문이 break를 만나지 않고 범위 전체를 반복했을 때
# else 블록이 실행
# 반복문 중간에 break를 만나면 else는 실행되지 않음.
for i in range(5):
    if i == 3:
        continue
    print(i, end=' ')
else: # else의 위치 중요 for-else 구문이다.
    print('모든 반복을 끝냄')

print()

# for-else 구문을 사용한 소수 찾기
for n in range(2,11):
    for divider in range(2,n):
        if n % divider == 0: # 약수가 존재 -> 소수가 아님.
            break
    else: # break를 만나지 않았을 때 -> 약수가 없음 -> 소수
        print(f'{n}은 소수다!')

