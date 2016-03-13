# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CqspiderItem(scrapy.Item):
    # define the fields for your item here like:
    project_name = scrapy.Field()
    bid_name = scrapy.Field()
    bid_money = scrapy.Field()
    bid_time = scrapy.Field()
