# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZdayeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proxy = Field()
