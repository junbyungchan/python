"""
csv 모듈을 import하지 않고 csv파일 사용
문자열 안에 쉼표가 들어가 있는 경우
"""
import csv
# 문자열(string)을 아이템으로 갖는 리스트
row1 = ['test1', 'success', 'Mon']
row2 = ['test2', 'failure, kind of', 'Tue']
row3 = ['test3', 'sucess, kind of', 'Wed']
result = [row1, row2, row3]
print(result)

# 파일을 쓰기 모드로 열기
# csv 파일을 쓸(write) 때는 불필요한 라인이 써지지 않도록 하기 위해서
# 파일을 오픈할 때 newline='' 파라미터를 추가!!
with open('test_result.csv', mode= 'w', encoding='UTF-8', newline='') as f:
    # csv writer 객체 생성
    writer = csv.writer(f, delimiter = ',') # 파일을 write 하려면 writer객체를 생성해야한다.
    for row in result:
        # writer 객체의 writerow() 메소드를 사용해서 한 줄씩 쓰기
        writer.writerow(row)
        # row1,2,3의 내용이 있는 test_result.csv 파일이 같은 경로에 생성됨.
        # delimiter=',' ===> ','가 있는 문장은 ""로 묶였고, 없으면 그냥 출력됨

# csv 모듈을 사용하지 않고 csv 파일을 읽었을 때 문제점
with open('test_result.csv', mode='r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip().split(','))
        # 'failure, kind of'라는 하나의 문자열이
        # 'failure' 와 'kind of'라는 두 개의 문자열로 쪼개짐
        # 원래 데이터에 없어야 할 "가 문자열에 포함됨
        # 예)
        # ['test1', 'success', 'Mon']
        # ['']  -----> 이것 처럼 이상한 데이터가 포함됨
        # ['test2', '"failure', ' kind of"', 'Tue'] -----> failure와 kind of가 다른 문자열로 쪼개짐
        # ['']
        # ['test3', '"sucess', ' kind of"', 'Wed']
        # ['']
print('\ncsv 모듈을 사용할 때')
with open('test_result.csv', mode='r', encoding='UTF-8') as f:
    # csv reader 객체를 생성
    reader = csv.reader(f)
    for row in reader:
        # reader 객체의 read 기능을 이용해서 한줄씩 읽음
        print(row)

