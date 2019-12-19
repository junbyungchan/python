"""
파이썬으로 HTML 문서 분석:
설치해야할 패키지(pip install package-name)
1) beautifulsoup4 : HTML 요소들을 분석하는 패키지
2) html5lib : HTML 문서를 parsing(분석)
3) requests : HTTP 요청(request)을 요청을 보내고 서버로부터 응답(response)을 받는 기능을 담당.
"""
from bs4 import BeautifulSoup

# 파일을 읽기모드로 열기
with open('web01.html',mode='r',encoding='UTF-8') as f:
    # HTML 문서를 파라미터에 전달해서, BeautifulSoup 객체 생성
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup) # HTML의 내용 전체 출력

    # HTML 요소들 중에서 'h1' 요소를 찾음
    h1 = soup.find('h1') # find('태그이름')
    print(h1)

    h2 = soup.h2 # soup.태그이름 - soup.find('h2') 와 동일한 의미
    print(h2)
    print(h2.string) # 앞뒤의 태그만 삭제해준다.

    # paragraph 요소 안의 문자열을 찾아서 출력.
    # text 속성은 자식 요소(child element) 태그들을 제거하고, 텍스트만 찾아줌.
    # print(soup.find('p').text)
    print(soup.p.text)

    # find는 HTML 문서를 처음부터 분석을 하다가 가장 처음에 만나는 요소를 리턴한다.
    # print(soup.find('a'))
    print(soup.a) # 그에 해당하는 한줄만 리턴해준다.

    # find_all은 HTML 문서 전체에서 찾은 모든 해당 요소들의 리스트를 리턴해준다.
    print(soup.find_all('a'))
    # print(soup('a')) # soup('태그이름')은 soup.find_all('태그이름')과 동일
    #  [<a href="https://www.daum.net/">다음 카카오</a>, <a href="https://www.naver.com">
    #  <img src="daum.png" style="width: 200px;"/>
    #  </a>]   ---> 리스트 형식!

    # HTML의 문서의 모든 링크에서 링크 주소(href)만 추출해서 출력
    for i in soup('a'):
        # HTML요소.get('attr이름') - attr의 값을 구함.
        print(i.get('href')) # get('태그이름')
