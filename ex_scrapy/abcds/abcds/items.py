# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbcdsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 제목
    title = scrapy.Field()

    # 본문
    text = scrapy.Field()

    # 이미지 URL
    img_url = scrapy.Field()

    # 등록일
    posted_date = scrapy.Field()
    pass
