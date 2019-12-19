"""
클래스 작성, 객체 생성, 메소드 사용 연습
"""

# 변수 이름이나 함수 이름을 한번에 바꾸려고 할 경우에
# Shift + F6 같이 누르자  -> continue -> do refactor 클릭 하면 모두 변경된다.

class emp:
    """
    field: empno, ename, salary, deptno
    method: raise_salary(self,pct)
    """
    def __init__(self,empno,ename,salary,deptno):
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno


    def raise_salary(self,pct):
        """
        인상된 급여를 리턴
        :param pct: 급여 인상율(0.1 = 10%, 0.5 = 50%)
        :return: 인상된 급여
        """
        self.salary = (1+pct) * self.salary
        # self.salary *= (1 + pct )
        print('인상된 급여 :')
        return self.salary


    def __repr__(self):
        return f'(사번:{self.empno},이름:{self.ename},급여:{self.salary},부서번호:{self.deptno})'


bc = emp(1010,'전병찬',240,10)
print(bc.__repr__())
print(bc.raise_salary(0.5))
print(bc.__repr__())

scott = emp(1011,'Scott',10000,20)
print(scott.__repr__())
scott.raise_salary(-0.1)
print(scott.__repr__())

ohssam = emp(1012,'오쌤',500,30)

employees = [ohssam,bc,scott]
print(employees)
print(sorted(employees,key=lambda x: x.empno))
print(sorted(employees,key=lambda x: x.salary))
print(sorted(employees,key=lambda x: x.ename))







