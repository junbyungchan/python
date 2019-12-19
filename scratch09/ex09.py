"""
emp.csv 파일을 읽어서, DataFrame을 생성
- 급여(sal)가 2000 이상인 직원들의 모든 정보를 출력
- 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
- 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력
- 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
- 20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름,
급여, 부서번호를 출력
- 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인
직원들의 모든 정보를 검색
- 사원 이름에 'E'가 포함된 직원들의 이름만 출력 (str.contains() 이용)
- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 데이터 프레임을 파일로 저장
"""

import pandas as pd

if __name__ == '__main__':
    file_path = 'emp.csv'
    # csv 파일을 pd.read_csv(파일 이름)으로 읽어서 emp 변수에 저장
    # pandas.read_csv() 함수는 csv 파일의 첫번째 줄을 헤더(컬럼 이름)으로 취급.
    # csv 파일의 첫번째 줄이 헤더(컬럼 이름이)가 아니고 실제 레코드인 경우에는,
    # header=None 파라미터를 추가해야함!!!!
    emp = pd.read_csv(file_path,  header = None )
    # 컬럼들을 0 1 2 3 4 5 6 7 로 임의로 만들어준다.
    #       0       1         2       3                    4       5       6   7
    # 0  7369   SMITH     CLERK  7902.0  1980-12-17 00:00:00   800.0     NaN  20
    # 1  7499   ALLEN  SALESMAN  7698.0  1981-02-20 00:00:00  1600.0   300.0  30
    # 2  7521    WARD  SALESMAN  7698.0  1981-02-22 00:00:00  1250.0   500.0  30
    # 3  7566   JONES   MANAGER  7839.0  1981-04-02 00:00:00  2975.0     NaN  20
    # 4  7654  MARTIN  SALESMAN  7698.0  1981-09-28 00:00:00  1250.0  1400.0  30


    print('shape: ', emp.shape) # --> 첫번째 데이터들이 컬럼 이름으로 들어가버리는 문제가 발생한다.
    print(emp.head())

    # DataFrame 컬럼 이름을 설정
    emp.columns = ['empno','ename','job','mgr','hiredate','sal','comm','deptno'] # 리스트 형식을 저장
    print(emp.iloc[0:2])
    print('=====================================================')


    print('\n급여(sal)가 2000 이상인 직원들의 모든 정보')
    print(emp[emp['sal'] >= 2000]) # boolean indexing //// DataFrame[조건식]

    print('\n부서 번호(deptno)가 10인 직원들의 모든 정보')
    print(emp[emp['deptno'] == 10])

    print('\n급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여')
    # select empno, ename, sal
    # from emp
    # where sal > (select avg(sal) from emp)
    subset = emp[ emp['sal'] > emp['sal'].mean() ]
    print(subset[['empno','ename','sal']])

    print('\n30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호')
    # select empno, ename, sal, deptno
    # from emp
    # where deptno = 30 and job = 'SALESMAN'
    c1 = emp['deptno'] == 30 # 30번 부서에서 일하는
    c2 = emp['job'] == 'SALESMAN' # 직책이 SALESMAN인
    subset = emp[c1 & c2] # and라고 표기하면 안되고 문자를 사용해여야 한다. '&'
    # subset = emp[(emp['deptno'] == 30) & (emp['job'] == 'SALESMAN')] 풀어서 쓴 것
    print(subset[['empno','ename','sal','deptno']])

    print('\n20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호')
    # select * from emp
    # where (deptno = 20 or deptno = 30) and sal > 2000;
    # select * from emp
    # where deptno in (20,30) and sal > 2000 ;

    c1 = emp['deptno'].isin([10,20]) # c1과 c2를 합친 것
    # c1 = emp['deptno'] == 20
    # c2 = emp['deptno'] == 30
    c3 = emp['sal'] > 2000
    subset = emp[c1 & c3]
    print(subset[['empno','ename','sal','deptno']])

    print('\n수당이 없는 직원들 중에서, 매니저가 있고, 직책이 MANAGER 또는 CLERK인 직원들의 모든 정보')
    c1 = emp['comm'].isna() # 수당이 없는 직원. emp['comm'] == 'NaN' 이라고 하면 안됨.
    c2 = ~emp['mgr'].isna() # mgr 컬럼의 값이 NaN(null)이 아닌경우
    # c3 = (emp['job'] == 'MANAGER' | (emp['job'] == 'CLERK')
    c3 = emp['job'].isin(['MANAGER','CLERK']) # job이 manager 또는 clerk
    subset = emp[c1 & c2 & c3]
    print(subset)

    print('\n사원 이름에 E가 포함된 직원들의 이름')
    # select ename from emp where ename like '%e%'
    #
    # r = []
    # for x in list:
    #     if x.contains('E'):
    #         r.append(True)
    #     else:
    #         r.append(False)

    # 판다스에서만 사용하는 문법이라고 생각하자. .str.contains
    # 앞의 series 중에서 각 원소마다를 string으로 생각해서 E가 포함 되어있는지를 확인하는 것
    subset = emp[emp['ename'].str.contains('E')]
    # 두개의 출력 내용이 다르다. ---> 그러므로 두 객체는 다른 것이므로 ---> 사용 방법도 달라진다. 주의하자
    print(subset['ename']) # Series // 각 아이템을 뽑아서 string 형식으로 저장해놓겠다.
    print(subset[['ename']]) # DataFrame // 컬럼 한개짜리 데이터 프레임!

    # Dataframe.to_csv(file 이름) : 데이터 프레임을 csv 파일로 저장하는 방법
    # to_csv(file name) 함수는 행 이름(row index)를 파일에 자동으로 쓴다.
    # row index를 파일에 쓰지 않으려면, 함수를 호출할 대 마다 index = False 파라미터를 추가하면 된다.
    emp.to_csv('emp2.csv', index = False)






