"""
file.write 메소드를 사용한 csv 파일 작성
"""
import os
import numpy as np

# 현재 폴더에 data 폴더 생성
# 여러번 실행하면 오류가 나므로 try-except로 처리
try:
    os.mkdir('data')
except FileExistsError:
    pass
    # 현재 폴더에 data 폴더가 있으면 아무일도 하지 않음음    pass

file_name = os.path.join('data','exam.csv')
print(file_name)

# 파일을 w 모드로 열기
with open(file_name, mode='w',encoding='utf-8') as output_file:
    output_file.write('id,언어,수리,과탐,사탐\n')
    for i in range(1,11):
        line = f'{i},{np.random.randint(0,101)}, {np.random.randint(0,101)}, {np.random.randint(0,101)}, {np.random.randint(0,101)} \n'
        output_file.write(line)
