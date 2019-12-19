import csv

import pandas as pd
import cx_Oracle

def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    # with-as 구문을 사용해서 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost',1521,'orcl')
    with cx_Oracle.connect('scott','tiger',dsn) as connection:
        # with-as 구문을 사용해서 Cursor 객체를 생성
        with connection.cursor() as cursor:
            # scratch09 패키지에서 작성한 테이플 전체 검색 함수를 사용해서,
            # emp_df 데이터 프레임을 생성
            sql = 'select * from emp'
            cursor.execute(sql)
            emp_df = [row for row in cursor]

            # emp_df를 csv 파일로 저장
            file_name = 'emp_df.csv'
            with open(file_name,'w',newline='',encoding='UTF-8') as f:
                writer = csv.writer(f)
                for item in emp_df:
                    writer.writerow(item)
    file_name = 'emp_df.csv'
    emp_df = pd.read_csv(file_name,header=None)
    emp_df.columns = ['EMPNO','ENAME','JOB','MGR','HIREDATE','SAL','COMM','DEPTNO']
    print(emp_df)

    # emp_df에서 부서별 평균 급여를 출력
    groupdeptno = emp_df.groupby('DEPTNO') # 부서별로 groupby
    sal_by_deptno = groupdeptno['SAL']

    mean_deptno = groupdeptno['SAL'].mean()
    print(mean_deptno)
    # emp_df에서 부서별 인원수를 출력
    count_deptno = groupdeptno['EMPNO'].count()
    print(count_deptno)
    # emp_df 부서별 급여 최솟값 출력
    min_deptno = groupdeptno['SAL'].min()
    print(min_deptno)
    # emp_df 부서별 급여 최댓값 출력
    max_deptno = groupdeptno['SAL'].max()
    print(max_deptno)
    # 위의 결과를 하나의 데이터 프레임으로 출력
    all_emp_df = pd.DataFrame({
        'mean_deptno': mean_deptno,
        'count_deptno': count_deptno,
        'min_deptno': min_deptno,
        'max_deptno': max_deptno
    })
    print(all_emp_df)

    # agg(), aggregate(): 파라미터에 함수 이름 (또는 리스트)을 전달하면,
    # GroupBy 객체에 함수를 적용함.
    # groupdeptno.mean() 과
    # groupdeptno.agg('mean')는 동알힌 동작
    # 함수가 집계 함수(pandas.Series 또는 pandas.DataFrame 클래스가 가지고 있는
    # 메소드들: count, mean, sum, ...)인 경우에는 함수 이름을
    # 문자열로 전달함.
    # 개발자가 작성한 함수는 함수 이름을 파라미터에 전달해야함.
    df = sal_by_deptno.agg(['count','mean','min','max', peak_to_peak])
    print(df)
    print('==========')

    # print(groupdeptno.agg(pd.Series.mean)) 코드를 쉽게 사용할 수 있도록
    # print(groupdeptno.agg('mean')) 코드와 같은 호출 방식도 제공.



    # emp_df에서 직책별 직원수, 급여 평균, 최소, 최댓값을 출력
    groupjob = emp_df.groupby('JOB') # 직책별로 groupby
    sal_by_job = groupjob['SAL']

    count_job = groupjob['SAL'].count()
    print(count_job)

    mean_job = groupjob['SAL'].mean()
    print(mean_job)

    min_job = groupjob['SAL'].min()
    print(min_job)

    max_job = groupjob['SAL'].max()
    print(max_job)

    print('================')
    print(sal_by_job.agg(['count','mean','min','max',lambda x: x.max() - x.min()]))
    # agg() 함수가 만드는 DataFrame의 컬럼 이름을 설정할 때는
    # keyword-argument 방식 또는 dict를 파라미터로 전달함.
    print(sal_by_job.agg(Count = 'count',
                         Average = 'mean',
                         Minimum ='min',
                         Maximum = 'max',
                         Range = lambda x: x.max() - x.min()))


    # emp_df에서 부서별, 직책(job)별 직원 수, 급여 평균, 최소, 최댓값 출력
    group_dept_job = emp_df.groupby(['DEPTNO','JOB'])
    sal_by_dept_job = group_dept_job['SAL']
    df = sal_by_dept_job.agg({
        'count' :'count',
        'average' :'mean',
        'maximum':'max',
        'minimum':'min',
        'range' : lambda x: x.max() - x.min()
    })

    # agg(),aggregate() 함수의 파라미터에 dict를 전달하는 방식은
    # pandas 패키지가 업그레이드 될때 없어질 수 있는 기능이다.(deprecated)
    # 따라서 dict 방식 보다는 keyword-argument 방식을 사용하는 것이 안전하다.

    print('================================================')
    print(df)

    count_dj = group_dept_job['EMPNO'].count()
    print(count_dj)

    mean_dj = group_dept_job['SAL'].mean()
    print(mean_dj)

    min_dj = group_dept_job['SAL'].min()
    print(min_dj)

    max_dj = group_dept_job['SAL'].max()
    print(max_dj)

