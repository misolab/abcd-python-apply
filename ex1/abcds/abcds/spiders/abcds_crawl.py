# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AbcdsCrawlSpider(CrawlSpider):
    name = 'abcds_crawl'

    # 크롤러 실행을 허용할 도메인을 지정 / 이외의 도메인은 무시
    allowed_domains = ['www.hanbit.co.kr']

    # 시작할 URL / 리스트로 지정하면 여러 웹페이지를 크롤링
    start_urls = [
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=001',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=003',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=004',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=005',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=006',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=007',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=008',

    ]

    # 어떻게 작동할지 규칙을 설정 / 시작URL의 모든 링크를 검산 후, 규칙에 맞는 링크가 있으면 콜백 메소드를 실행 / follow=True : 해당 페이지의 링크를 재귀적으로 반복
    rules = (
        Rule(
            # 크롤링할 링크를 정규 표현식으로 표현
            LinkExtractor(allow=r'store/books/look.php\?p_code=.*'),
            # 해당 링크가 오면 실행할 콜백 메소드
            callback='parse_item',
            # True이면 응답에 다시 한번 rules를 적용해 재귀 호출
            follow=True),
        # 반복적으로 계속 지정 가능함
        Rule(LinkExtractor(allow=r'store/books/category_list\.html\?page\d+&cate_cd=00\d+&srt=p_pub_date'))
    )

    def parse_item(self, response):
        i = {}
        i['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()
        i['book_author'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : '
                                          '"]/span/text()').extract()
        i['book_translator'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text('
                                              ')="번역 : "]/span/text()').extract()

        i['book_pub_date'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 '
                                            ': "]/span/text()').extract()

        i['book_isbn'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : '
                                        '"]/span/text()').extract()
        return i
