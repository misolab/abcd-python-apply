# [SCRAPY](https://scrapy.org/)
크롤링을 좀더 편하게 해주는 라이브러리

### 적용 방법
* pip3 install scrapy
* scrapy startproject abcds
* cd abcds
* items.py 편집
    * 발췌할 항목 설정 
    * <pre><code>name = scrapy.Field()</code></pre>
* scrapy genspider abcds_crawl abcds.kr
* spirders/abcd_crawl.py
    * parse 함수에 발췌할 항목 찾아 item 매핑
    * xpath 
        * html에 접근하는 (CSS선택자보다 ) 괜찬은 방법
        * 참고 사이트 : [xpath의 개념과 문법](http://twinbraid.blogspot.kr/2015/02/xpath.html)
        * 크롬 개발자 도구 > Copy > Copy XPath
* scrapy crawl abcds_crawl -o ../../result.csv -t csv


### 참고자료
* [[Python] scrapy를 이용한 크롤링](http://excelsior-cjh.tistory.com/m/entry/04-Scrapy%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%89%B4%EC%8A%A4%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0)
* [04. Scrapy를 이용한 뉴스 크롤링 하기](http://excelsior-cjh.tistory.com/m/entry/04-Scrapy%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%89%B4%EC%8A%A4%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0)