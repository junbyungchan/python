# open
f = open('test.txt',mode='r',encoding='utf-8')
# read: read(), readline()
# content = f.read(n) # 문서 전체를 읽음. n개의 문자를 읽는다.
# print(content)

content_line = f.readline()
print(content_line)
# close
f.close()

f = open('test2.txt',mode='r', encoding='utf-8')
# readline(): 파일에서 한줄씩 읽음
# 줄바꿈 문자('\n')까지 읽음!
line = f.readline()
line = line.strip() # 문자열이 있을때 앞뒤의 공백을 잘라내라. # 그래서 \n를 불포함 하므로 length: 18
print(f'line: {line}, length: {len(line)}') # 18글자 + \n 포함해서 length: 19
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
f.close()


# 무한루프와 realine()을 사용해서 문자 끝까지 읽기
f = open('test2.txt',mode= 'r',encoding='utf-8')
while True: # 무한 루프
    line = f.readline()
    # read(),readline()은 문서 끝에 도달하면 빈 문자열('')을 리턴
    if line == '': # 파일 끝(EOF:End Of File)에 도달
        break # 무한 루프 종료
    print(line.strip())

f.close()

f = open('test.txt',mode='r',encoding='utf-8')
line = f.readline()
while line: # 문자열이 비어있으면('') False / 문자열이 비어있지 않으면 True
    print(line.strip()) # 출력
    line = f.readline() # 다음 줄의 문자열을 line에 전달

f.close()



with open('test2.txt',mode='r',encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()







