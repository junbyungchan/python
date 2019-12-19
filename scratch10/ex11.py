"""
웹 주소(URI, URL) 의 형식:
프로토콜://서버주소[:포트번호(주로생략함)]/경로?쿼리스트링
http://www.naver.com
https://www.naver.com/webtoon/
https://comic.naver.com/webtoon/detail.nhn?titleId=183559&no=459&weekday=mon
쿼리스트링(query string): 클라이언트(브라우저)가 서버로 보내는 정보
    parameter= param 값 형식으로 작성
    파라미터가 여러개일 경우에는 &로 파라미터들을 구분

www.daum.net에서 '머신러닝' 검색 기사 중, 기사 100개의 URL 주소와 제목 출력

다음에서 임의의 검색어(키워드)로 검색한 기사 100개의 URL 주소가 기사 제목을 출력하는
함수수
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 내 답안
    # for i in range(1,11):
    #     url = f'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p={i}'
    #     print('=====')
    #     html = requests.get(url).text.strip()
    #
    #     soup = BeautifulSoup(html,'html5lib')
    #
    #     news_link = soup.select('.coll_cont ul li a.f_link_b')
    #     for j in news_link:
    #         print(j.get('href'),j.text.strip())

    print('-----------------------------------------------------------')
    # 강사님 답안
    # url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0'
    for page in range(1,11):
        print(f'=== Page {page} ===')
        # page_url = url + str(page)
        # print(page_url)
        # 해당 페이지 URL 주소로 GET 방식 요청을 보내고,
        # 서버에서 보낸 응답(response)을 문자열로 처리
        # html = requests.get(page_url).text.strip()
        response = requests.get(url, params={'p': page})
        # requests.get(url, params = {key: value}) :
        #   params의 내용을 url의 query string의 파라미터로 추가해준다.
        #   url?...&key=value
        html = response.text.strip()

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')
        news_links = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_links:
            # HTML 요소(element)의 href 속성(attribute) 값을 읽음
            news_url = link.get('href')
            # HTML 요소가 가지고 있는 컨텐트 문자열 
            news_title = link.text.strip()
            print(news_url,news_title)
