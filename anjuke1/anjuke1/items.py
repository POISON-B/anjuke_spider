# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Anjuke1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    address = scrapy.Field()
    info = scrapy.Field()
    types = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()