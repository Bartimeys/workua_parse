# -*- coding: utf-8 -*-
import scrapy


class WorkuaItem(scrapy.Item):
    vacancy = scrapy.Field()
    company = scrapy.Field()
    time = scrapy.Field()
    description = scrapy.Field()

