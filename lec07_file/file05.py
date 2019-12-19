"""
file open 모드(mode)
    r: read, 읽기 모드
       읽기모드는 파일이 없으면 FileNotFoundError가 발생
    w: write, 쓰기 모드
       쓰기모드는 파일이 없으면, 새로운 파일을 생성함
       파일이 있으면, 기존 파일을 열어줌. 단, 기존 파일의 내용이 삭제됨.
       ** 덮어쓰기(overwrite)가 되버림 **
    a: append, 추가 모드
       추가모드에서 write()를 하면 뒷부분에 추가만 된다.
       추가모드는 파일이 없으면, 새로운 파일을 생성해준다.
       파일이 있으면, 기존 파일의 가장 마지막에 file pointer가 위치하고,
       새로운 내용은 파일 끝에서부터 추가(append)된다.
"""
try:
    with open('Nofile.txt',mode='r') as f:
        pass
except FileNotFoundError:
    pass

with open('Newfile.txt',mode='w',encoding='utf-8') as f:
    # f.write('test 테스트 ...')
    pass  # 아무일도 하지 않더라도 파일의 내용이 삭제됨.

with open('Append.txt',mode='a',encoding='utf-8') as f:
    f.write('test 줄바꿈\n')

with open('Append.txt',mode='a',encoding='utf-8') as f:
    f.write('추가 ...\n')