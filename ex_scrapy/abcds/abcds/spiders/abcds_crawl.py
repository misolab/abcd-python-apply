# -*- coding: utf-8 -*-
import scrapy

from abcds.items import AbcdsItem


class AbcdsCrawlSpider(scrapy.Spider):
    name = 'abcds_crawl'
    allowed_domains = ['abcds.kr']
    start_urls = ['http://abcds.kr/']

    def parse(self, response):
        articles = response.xpath("//*[@id=\"wrap\"]/div[2]/div/main/article")

        for article in articles:
            item = AbcdsItem()
            item['title'] = article.xpath("header/h2/a/text()").extract()
            item['text'] = article.xpath("div/p/text()").extract()
            item['img_url'] = article.xpath("header/div/img/@src").extract()
            item['posted_date'] = article.xpath("header/p/time/a/text()").extract()

            yield item
