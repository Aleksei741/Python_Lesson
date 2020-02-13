# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from bs4 import BeautifulSoup as bs


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://izhevsk.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy = response.css(
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)'
        ).extract()

        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        html = bs(response.text, 'lxml')
        link = response.url
        name = response.css('div.vacancy-title h1.header::text').extract_first()
        #salary = response.css('div.vacancy-title p.vacancy-salary::text').extract()
        salary = html.find('p', {'class': 'vacancy-salary'}).text
        # print(name, salary)
        #print(response.url)
        #print(salary)
        #yield JobparserItem(name=name, salary=salary)
        yield JobparserItem(name=name, salary=salary, link=link, source='hh.ru')


