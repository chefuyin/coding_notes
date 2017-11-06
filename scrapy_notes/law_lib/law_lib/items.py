# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LawLibItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title=scrapy.Field()
    publish_date=scrapy.Field()
    department=scrapy.Field()
    law_lib_url=scrapy.Field()
    source_url=scrapy.Field()
    publish_number=scrapy.Field()
    invalid_date=scrapy.Field()
    content=scrapy.Field()