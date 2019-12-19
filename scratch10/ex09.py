from bs4 import BeautifulSoup

with open('web02.html',mode='r',encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)

    # HTML 문서 안의 모든 div 태그를 찾음
    for i in soup('div'): # soup('div') 와 soup.find_all('div')는 동일
        print(i.text)

    # HTML 문서 안의 'class1' 클래스 속성을 갖는 모든 요소들을 찾는다.
    # soup(attrs={attr이름: attr값})
    # soup.find_all(attrs={attr이름: attr값})
    # 위의 두개는 동일한 기능
    for i in soup(attrs={'class':'class1'}):
        print(i)
    print('===========')
    # HTML 문서 안의 "class2" 클래스 속성을 갖는 모든 요소들을 찾는다.
    for i in soup(class_='class2'):
        print(i)

    # HTML 문서 안의 'id1' 아이디 속성을 갖는 요소를 찾는다.
    for i in soup(id_='id1'):
        print(i)
    # print(soup.find(attrs={'id':'id1'})) 같은 의미
    print(soup.find(attrs={'id': 'id1'}))
    print(soup.find(id='id1'))
    print(soup(id='id1')[0].text) # soup.find_all(id='id1') ---> 리스트다!