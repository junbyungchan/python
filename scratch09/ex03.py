"""
1) csv 파일(stock_price.csv) write
6/20/2019,AAPL,90.91
6/20/2019,MSFT,41.68
6/21/2019,AAPL,90.86
6/21/2019,MSFT,41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
   각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
   각 주식 종목의 주식 가격 평균을 계산해서 출력
"""

import csv


row1 = ['6/20/2019','AAPL','90.91']
row2 = ['6/20/2019','MSFT','41.68']
row3 = ['6/21/2019','AAPL','90.86']
row4 = ['6/21/2019','MSFT','41.51']
result = [row1,row2,row3,row4]
with open('stock_price.csv', mode='w', encoding='UTF-8',newline='') as f:
    writer = csv.writer(f,delimiter=',')
    for row in result:
        writer.writerow(row)

with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    # csv.reader 객체를 생성
    reader = csv.reader(f)
    # 파일에 한 줄씩 반복하면 읽어서 리스트에 추가
    df = [row for row in reader]
print(df)

# 'AAPL' 종목의 주식 가격들의 리스트
aapl_prices = [float(item[2]) for item in df
               if item[1]=='AAPL']
print(aapl_prices)
aapl_mean = sum(aapl_prices) / len(aapl_prices)
print(aapl_mean)

msft_prices = [float(item[2]) for item in df
               if item[1]=='MSFT']
print(msft_prices)
msft_mean = sum(msft_prices) / len(msft_prices)
print('msft_mean:', msft_mean)

with open('stock_price.csv', mode = 'r' , encoding='UTF-8') as f:
    # csv.DictReader 객체를 생성
    # csv 파일에는 컬럼 이름이 없는 경우,
    # 생성자의 fieldnames 파라미터에 컬럼 이름 값들을 전달하면 됨.
    col_names = ['date','stock','price']
    reader = csv.DictReader(f, fieldnames=col_names)
    df = [row for row in reader]
print(df)
aapl_prices = [float(item['price']) for item in df
               if item['stock'] == 'AAPL']
print(aapl_prices)
aapl_mean = sum(aapl_prices) / len(aapl_prices)
print('aapl_mean:', aapl_mean)

msft_prices = [float(item['price']) for item in df
               if item['stock'] == 'MSFT']
print(msft_prices)
msft_mean = sum(msft_prices) / len(msft_prices)
print('msft_mean:', msft_mean)























