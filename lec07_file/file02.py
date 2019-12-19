"""
1) 파일 열기(open)
2) 파일 읽기(read)/쓰기(write)
3) 파일 닫기(close)
"""

# 파일 열기
f = open('test.txt',mode= 'w',encoding='UTF-8')

# 파일에 텍스트를 씀
for i in range(1,11):
    f.write(f'{i}번째 줄...\n')

# 파일 닫기 // 파일은 열었으면 닫아야만 다음에 파일을 다시 열 수 있다.
f.close()

# with 구문: 리소스를 사용한 후 close() 메소드를 자동으로 호출
# with ... as 변수 :
#      실행문
with open('test2.txt',mode='w',encoding='utf-8') as f :
    f.write('Hi Annyunghasaeyo!\n')
    f.write('하이 안녕하세요!\n')
    f.write('Nǐ hǎo\n')