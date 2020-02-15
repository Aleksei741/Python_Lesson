# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


def parameters_values_correct(values):
    values = values.replace('\n', '')
    values = values.replace('  ', '')
    return values

def price_correct(values):
    values = int(values)
    return values


class LeroymerlinItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())

    #price = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(price_correct))
    currency = scrapy.Field(output_processor=TakeFirst())#Валюта
    unit = scrapy.Field(output_processor=TakeFirst())#за что

    description = scrapy.Field(output_processor=TakeFirst())
    #description = scrapy.Field(output_processor=MapCompose(description_correct))
    parameters_names = scrapy.Field()
    parameters_values = scrapy.Field(output_processor=MapCompose(parameters_values_correct))

    photo_link = scrapy.Field()
    photo_path = scrapy.Field()
    pass
