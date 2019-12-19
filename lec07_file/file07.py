"""
file.readline() 사용해서 csv 파일 읽기
"""

def my_csv_reader(fn : list, header = True) -> list:
    """
    csv 파일의 데이터를 2차원 배열 형태로 리턴

    :param fn: 읽을 파일 이름(예: data\\exam.csv)
    :param header : csv 파일의 헤더 존재 여부
    :return: csv 파일 헤더는 제외한 데이터들로 이루어진 2차원 리스트
    """
    list = []
    with open('data\\exam.csv',mode = 'r',encoding='utf-8') as fn:
        fn.readline()
        for line in fn:
            # line = line.strip()
            # line = line.split(',')
            list.append(line.strip().split(','))

    et = []
    for i in list:
        for j in i:
            et.append(int(j))
    n = 5
    et = [et[i * n:(i + 1) * n] for i in range((len(et) + n - 1) // n)]


    return et

def print_data(data:list) -> None:
    """
    2차원 리스트의 내용을 출력
    ex)
    1 10 20 30 40
    2 11 21 31 41
    ...
    :param data: 2차원 행렬 형태의 리스트
    :return: None
    """

    for i in data:
        for j in i:
            print(j, end=' ')
        print()


def get_sum_mean(data: list, col: int) -> tuple :
    """
    주어진 2차원 리스트(data)에서 해당 컬럼(col)의 데이터들의
    총합(sum)과 평균(mean)을 계산해서 리턴하는 함수

    :param data: 2차원 행렬 형태의 리스트
    :param col: 컬럼 인덱스(0, 1, 2, ...)
    :return: 컬럼 데이터의 합과 평균을 리턴
    """
    abc = []
    for i in data:
        abc.append(i[col])

    sum_abc=sum(abc)
    avg_abc=sum(abc)/len(abc)
    print(sum_abc)
    print(avg_abc)


if __name__ == '__main__':

    # 코드들 테스트하기
    d = my_csv_reader('data\\exam.csv')
    print_data(d)
    get_sum_mean(d,col=2)
