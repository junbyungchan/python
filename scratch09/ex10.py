import cx_Oracle
import pandas as pd

def get_column_names_of(table,cursor):
    # sql =f"select column_name from user_tab_columns where table_name = '{table.upper()}' order by column_id"
    # cursor.execute(sql)
    sql = """ select column_name from user_tab_columns
    where table_name = :tbl_name
    order by column_id"""
    cursor.execute(sql, tbl_name = table.upper()) # data binding 방식
    # cursor가 sql 문장의 :변수 위치에 데이터 타입에 맞게끔 값을 치환해 준다.
    # 값이 문자열이면 '문자열' 형태로 :변수 위치에 치환된다.
    col_names = [row[0] for row in cursor]
    return col_names

def select_all_from(table,cursor):
    sql = f"""
            select *
            from  {table.upper()}
            """
    # from 구문에서 테이블 이름은 ''로 감싸면 안되기 때문에
    # data binding 방식을 사용할 수 없다.
    cursor.execute(sql)
    e = []
    # for row in cursor:
    #     e.append(row) # 리스트를 만들어서
    e = cursor.fetchall() # [row for row in cursor]

    # 데이터 프레임에 컬럼 이름 설정
    df = pd.DataFrame(e, columns= get_column_names_of(table,cursor)) # 데이터 프레임에 넣는 방법
    # df.columns = [get_column_names_of(table,cursor)]
    return df

if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost',1521, 'orcl')
    with cx_Oracle.connect('scott','tiger',dsn) as connection:
        # cursor 객체 생성
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of( 'emp' , cursor)
            print(emp_columns) # ['empno','ename','job',....]

            emp_df = select_all_from('emp', cursor) #  pandas.DataFrame
            # DataFrame은 컬럼 이름(인덱스)가 포함되어 있어야 함.
            print(emp_df)

            dept_df = select_all_from('dept',cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade',cursor)
            print(salgrade_df)

            # DataFrame에 새로운 컬럼을 추가
            # DataFrame['컬럼 이름'] = list , pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['sal'] 개수만큼  대해서 반복:
            # 선택된 sal 값이 salgrade_df의 어느 grade에 속하는 지를 찾음
            # -> salgrade_df의 행 개수 만큼 반복하면서 LO, HI와 비교
            # -> DataFrame.iterrows() 함수 : 데이터 프레임의 튜플(행 이름, 행)을 반복문 안에서 사용할 수 있게 해줌.
            sal_grade = []  # 급여 등급을 저장할 list
            for sal in emp_df['SAL']:
                for _ , row in salgrade_df.iterrows(): # iterrows() 함수는 행의 번호(이름)과  해당 하는 행을 반환해준다.
                    if row['LOSAL'] <= sal <= row['HISAL']:
                        # 급여 등급을 찾은 경우
                        sal_grade.append(row['GRADE'])
                        break # salgrade_df 반복을 중지
            emp_df['SAL_GRADE'] = sal_grade # DataFrame에 새로운 컬럼 추가
            print(emp_df)

            # SQL join - pandas.merge
            emp_dept = pd.merge(emp_df, dept_df, on= 'DEPTNO')
            print(emp_dept)

            # pandas.merge(left, right, how, on, left_on, right_on, ...)
            # Left, right : 조인할 데이터 프레임
            # how: 조인방식(inner,left,right)
            # on : 조인할 때 기준이 되는 컬럼 이름
            # 조인의 기준이 되는 컬럼 이름이 데이터 프레임마다 다르면,
            # left_on  = 'left 데이터 프레임의 컬럼 이름' , right_on = 'right 데이터 프레임의 컬럼 이름'

            # emp_df, dept_df 데이터 프레임의 left, right join 결과 비교
            # left join의 결과
            emp_dept_left = pd.merge(emp_df, dept_df, how= 'left', on='DEPTNO')
            print(emp_dept_left)
            # right join의 결과
            emp_dept_right = pd.merge(emp_df, dept_df, how='right', on='DEPTNO')
            print(emp_dept_right)

            # emp 테이블에서 mgr과 empno가 일치하는 join
            # 1) inner, 2)left , 3) right join
            # 1) inner
            emp_self_inner = pd.merge(emp_df, emp_df, how= 'inner', left_on= 'EMPNO', right_on='MGR')
            print(emp_self_inner)
            # 2) left
            emp_self_left = pd.merge(emp_df, emp_df, how= 'left', left_on= 'EMPNO', right_on='MGR')
            print(emp_self_left)
            # 3) right
            emp_self_right = pd.merge(emp_df, emp_df, how= 'right', left_on= 'EMPNO', right_on='MGR')
            print(emp_self_right[['EMPNO_x','ENAME_x','MGR_x','EMPNO_y','ENAME_y']])












