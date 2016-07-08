# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_info = scrapy.Field()
    book_isbn = scrapy.Field()
