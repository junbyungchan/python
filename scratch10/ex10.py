import requests
from bs4 import BeautifulSoup

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'

# 사이트(Web 서버)로 요청(request)를 보냄
html = requests.get(url).text.strip() # 요청의 결과(응답, response)를 저장
# print(html[0:100]) # 전체 문자열에서 100자만 확인하겠다.

# BeautifulSoup 객체를 생성
soup = BeautifulSoup(html , 'html5lib')

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# HTML 에서는 class는 여러개가 존재할 수도 있지만
# id는 단 하나만을 지칭할때 사용하는 것을 권장한다.

# 관심 있는 링크(뉴스 링크)들만 찾을 수 있는 방법을 고민
div_coll_cont = soup.find_all(attrs={'class':'coll_cont'})
# soup.find_all(class_='coll_cont')
print(len(div_coll_cont)) # 같은 클래스 이름이 있는 모든 HTML 요소들을 찾는다.

print()
# HTML 하위 요소(sub/child element)를 찾는 방법:
# 1) parent_selector > child_selector
#       div > ul > li   태그 이름
#       .coll_cont > #clusterResultUL > .fst   앞에 .을 붙이는 것은 class 이름이다. #을 붙이는 것은 id의 이름이다.
# 2) ancestor_selector(조상 선택자) descendant_selector(자손 선택자)
#       div li  (중간에 공백을 주면 된다.) // (div의 자손 요소들 중 li들)
#       .coll_cont .fst  (중간에 공백을 주면 된다.) // (클래스 .coll_cont 요소의 자손 요소들 중 클래스가 .fst인 요소들)
# soup.select(css_selector): soup 객체에서 CSS 선택자로 요소들을 찾는 방법
news_link = soup.select('.coll_cont ul li a.f_link_b')  # class .coll_cont 아래에 ul 아래에 li 아래에 a태그의 클래스 이름이 f_link_b 인 것을 선택
for link in news_link:
    print(link.get('href')) # href 태그만 가지고 온다.


