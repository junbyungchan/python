"""
lec08_database 패키지의 내용들을 참고해서,
오라클 데이터베이스에서 emp 테이블의 모든 레코드를 검색(select) -> 2차원 리스트
csv 모듈을 사용해서, csv 파일(emp.csv)로 저장
"""


import csv
import cx_Oracle

if __name__ == '__main__':
    # DSN = Data Source Name (접속할 오라클 서버(호스트) 정보)
    dsn = cx_Oracle.makedsn('localhost',1521, 'orcl') #sql developer 접속 정보를 확인하자
    # makedsn(호스트 이름, 포트, S_id)
    # 1.오라클 데이터베이스 서버에 접속(connection)
    with cx_Oracle.connect('scott','tiger',dsn) as connection:
        # cx_Oracle.connect('scoot','tiger',dsn) -> (아이디, 비밀번호, 서버이름)
        # 2. Cursor 객체(SQL문을 데이터베이스 서버에서 실행시키는 객체) 생성
        with connection.cursor() as cursor:
            # SQL 문장 장석
            sql_select_emp = 'select * from emp'
            # SQL 문장을 DB 서버에서 실행
            cursor.execute(sql_select_emp)
            # SQL 문장 실행 결과 처리
            emp = [row for row in cursor]
            # for row in cursor:
            #     print(row)
            print(emp[0])
            print(len(emp))


    # 리스트 emp의 내용을 파일에 csv 형식으로 저장
    file_path = 'emp.csv'
    with open(file_path,mode='w',encoding='UTF-8', newline='') as f:
        # newline='' 불필요한 줄을 없애겠다는 의미.
        # csv writer 객체를 생성
        writer = csv.writer(f)
        for item in emp: # 리스트의 각 아이템마다 반복
            writer.writerow(item) # 아이템을 csv파일에 한 줄씩 쓰기