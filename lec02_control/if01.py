# 19.11.05 Python Class 11
"""
if문

if 조건식:
    조건이 참일때, 실행할 문장

if 조건식:
    참일때 실행할 문장
else:
    거짓일때 실행할 문장

if 조건식1:
    조건식 1이 참일때 실행할 문장
elif 조건식2:
    조건식2가 참일때 실행할 문장
else:
    1, 2 둘다 거짓일때 실행할 문장

"""
# 숫자를 받아 양수인 경우에만 출력
num = int(input('input number >>>'))

if num > 0:
    print(f'num = {num}')
else:
    print('try again')
print('END')

# 성적 등급 나누기
score = 85

if score > 90:
    print('A')
elif score > 80:
    print('B')
elif score > 70:
    print('C')
else:
    print('D')

    # if,elif, else 블록 안에서 또 다른 if 구문을 사용할 수도 있음.
    if num % 2 == 0: # 짝수이면
        if num % 4 ==0:
            print('4의 배수')
        else:
            print('4의 배수가 아닌 짝수')
        pass # TODO: 짝수이면 할 일
    else: # 홀수이면
        print('홀수')
    print('프로그램 종료')