# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import re
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python&geo[c][0]=1']

    def parse(self, response: HtmlResponse):
        html = bs(response.text, 'lxml')
        pattern_next_page = re.compile('icMQ_ _1_Cht _3ze9n f-test-button-dalshe.*')
        next_page = html.find('a', {'class': pattern_next_page})['href']
        yield response.follow(next_page, callback=self.parse)

        vacancy_block = html.find('div', {'style': "display:block"}).findChildren('div', {
            'class': '_3zucV _2GPIV f-test-vacancy-item i6-sc _3VcZr'}, recursive=False)

        for vacancy in vacancy_block:
            pattern_vacancy_link = re.compile('icMQ_ _1QIBo f-test-link.* _2JivQ _3dPok')
            link = vacancy.find('a', {'class': pattern_vacancy_link})['href']
            yield response.follow(link, callback=self.vacansy_parse_sj)

    def vacansy_parse_sj(self, response: HtmlResponse):
        html = bs(response.text, 'lxml')
        name = html.find('h1', {'class': '_3mfro rFbjy s1nFK _2JVkc'}).text
        salary = html.find('span', {'class': '_3mfro _2Wp8I ZON4b PlM3e _2JVkc'}).text
        link = response.url
        #print('SupeJop', name, salary)

        yield JobparserItem(name=name, salary=salary, link=link, source='superjob.ru')

