import pandas as pd
import numpy as np

def squares(x):
    return x ** 2


def doubles(x):
    return x* 2


if __name__=='__main__':
    result1, result2 = squares(3) , doubles(3)
    print(result1, result2)

    array = np.array([1,2,3])
    result1, result2 = squares(array), doubles(array)
    print(result1,result2)

    # numbers = [[1,4],[2,5],[3,6]]
    # squares(numbers) # 오류 남


    df = pd.DataFrame({
        'a':[1,2,3],
        'b':[4,5,6]
    })
    print(df)
    print(squares(df))
    print(doubles(df))

    result = df.apply(squares)
    print(result)

    print(np.sum([1,2,3]))
    result = df.apply(np.sum, axis=1)
    print(result)
    result = df.apply(np.sum, axis=0)
    print(result)
    # DataFrame.apply(function, axis)
    # axis = 0(기본값)일 때는 , DataFrame의 각 컬럼을 함수의 파라미터에 전달함.
    # axis = 1일 때는, DataFrame의 각 행(row)을 함수의 파라미터에 전달함.
    # 함수의 리턴 값을 돌려받음.

    emp = pd.read_csv('emp_df.csv')
    emp.columns = ['EMPNO', 'ENAME', 'JOB', 'MGR', 'HIREDATE', 'SAL', 'COMM', 'DEPTNO']
    print(emp.agg(np.mean)) # 집계 함수는 숫자 타입의 컬럼만 자동으로 선택
    # emp.apply(np.mean)
    # apply 함수는 모든 컬럼 또는 행을 함수의 파라미터에 전달하기 때문에,
    # 집계 함수(mean, sum, ...)가 제대로 동작하지 않을 수도 있음.

