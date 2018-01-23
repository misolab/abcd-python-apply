import urllib.request
from bs4 import BeautifulSoup


#   pip3 install beautifulsoup4


url = "http://abcds.kr"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


# DOM 접근 (<html><body><p>)
p1 = soup.html.body.p
print("p1 - " + str(p1))
print("p1.string - " + p1.string)


# id요소로 접근
'''
a = soup.find(id="menu-item-1774").a
print("#menu-item-1774 - " + str(a))
print("#menu-item-1774.a.string - " + a.string)

# find("a")를 할 경우 <a>의 첫번째를 가져옵니다.    


# 태그명으로 찾기
links = soup.find_all("a")
for link in links:
    print(link)
    print("href :" + link.attrs['href'])
    print("text :" + str(link.string))
    print("=" * 10)
'''


# CSS 선택자로 접근
'''
menu_items = soup.select("li.menu-item")
for item in menu_items:
    print(item)
    link = item.a
    print("href :" + link.attrs['href'])
    print("text :" + str(link.string))
    print("=" * 10)


# 1개만 찾을때는 select_one
item = soup.select_one("li.menu-item-1112")
print(item)
link = item.a
print("href :" + link.attrs['href'])
print("text :" + str(link.string))
print("=" * 10)
'''