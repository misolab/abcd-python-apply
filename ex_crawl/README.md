
### 스크래핑 VS 크롤링
* 스크래핑
    * 웹사이트의 특정 정보(원하는 정보)를 추출하는 기술
    * 구조를 분석하는 것도 포함
* 크롤링 : Crwaling
    * 웹사이트를 정기적으로 돌며 정보를 추출하는 기술
    * 크롤러(Crawler) 혹은 스파이더 (Spider)
    * ex. 웹사이트의 링크를 정기적으로 타고 돌며 데이터를 긁어 데이터베이스에 저장
    
    
### 방법
* url.request + BeautifulSoup + persistence(file, db, …)
* BeautifulSoup이란
    * html에 탐색 및 조작에 편리한 라이브러리
    * [BeautifulSoup 사용법 예제](https://godoftyping.wordpress.com/2017/06/24/python-beautifulsoup/)
    * [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    #### pip3 install beautifulsoup4