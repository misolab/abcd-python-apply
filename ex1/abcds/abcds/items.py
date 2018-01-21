# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbcdsItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()

    posted_date = scrapy.Field()

    pass

