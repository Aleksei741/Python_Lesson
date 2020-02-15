# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroymerlin.items import LeroymerlinItem

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['http://leroymerlin.ru/']

    def __init__(self, mark):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={mark}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[contains(@class, 'paginator-button next-paginator-button')]/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//div[contains(@class, 'ui-sorting-cards')]//a[contains(@class, 'black-link product-name-inner')]/@href").extract()

        for link in links:
            link_=link
            yield response.follow(link_, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroymerlinItem(), response=response)
        loader.add_xpath('name', '//h1/text()')

        loader.add_xpath('price', "//uc-pdp-price-view/span[contains(@slot, 'price')]/text()")
        loader.add_xpath('currency', "//uc-pdp-price-view/span[contains(@slot, 'currency')]/text()")  # Валюта
        loader.add_xpath('unit', "//uc-pdp-price-view/span[contains(@slot, 'unit')]/text()")  # за что

        loader.add_xpath('description', "//uc-pdp-section-vlimited[contains(@class, 'section__vlimit')]/div/p/text()")
        loader.add_xpath('parameters_names', "//uc-pdp-section-vlimited[contains(@class, 'section__vlimit')]/dl/div/dt/text()")
        loader.add_xpath('parameters_values', "//uc-pdp-section-vlimited[contains(@class, 'section__vlimit')]/dl/div/dd/text()")

        loader.add_xpath('photo_link', "//picture[contains(@slot, 'picture')]/img[contains(@itemprop, 'image')]/@src")

        yield loader.load_item()