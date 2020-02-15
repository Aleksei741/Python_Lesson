# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def salary_correct(value):
    return value.replace('\xa0', ' ')

class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    salary = scrapy.Field(input_processor=MapCompose(salary_correct), output_processor=TakeFirst())
    source = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    pass
